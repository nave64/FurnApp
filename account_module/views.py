import sys
import io
import random

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.urls import reverse

from account_module.forms import RegisterFormSecond, OTPVerificationForm, LoginForm, ForgetPasswordForm, ResetPasswordForm
from account_module.models import User
from utils.phone_service import send_registration_sms, send_reset_password_sms, generate_otp_code
from django.conf import settings

# Fix stdout encoding to utf-8 for Persian text (important)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterFormSecond()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)

    def post(self, request):
        register_form = RegisterFormSecond(request.POST)
        if register_form.is_valid():
            user_phone = register_form.cleaned_data.get('phone')
            user_password = register_form.cleaned_data.get('password')
            token = generate_otp_code()  # 6 digit OTP code
            print(f"Generated OTP: {token}")

            existing_user = User.objects.filter(mobile__iexact=user_phone).exists()

            if existing_user:
                register_form.add_error('phone', 'شماره موبایل وارد شده تکراری می باشد')
            else:
                new_user = User(
                    username=user_phone,
                    mobile=user_phone,
                    email_active_code=token,
                    is_active=False,
                )
                new_user.set_password(user_password)
                new_user.save()

                # Send SMS using the new service
                sms_result = send_registration_sms(user_phone, token)
                
                if not sms_result['success']:
                    messages.error(request, sms_result['message'])
                    new_user.delete()
                    return render(request, 'account_module/register.html', {'register_form': register_form})

                # Save pending phone number in session
                request.session['pending_user'] = user_phone
                return redirect(reverse('otp_verify_page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register.html', context)


class OTPVerificationView(View):
    def get(self, request):
        form = OTPVerificationForm()
        return render(request, 'account_module/otp_verify.html', {'form': form})

    def post(self, request):
        form = OTPVerificationForm(request.POST)
        phone = request.session.get('pending_user')
        user = User.objects.filter(mobile=phone).first()

        if not phone or not user:
            messages.error(request, 'کاربری برای تایید یافت نشد. لطفاً مجدد ثبت‌نام کنید.')
            return redirect('register_page')

        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            if str(user.email_active_code) == str(otp):
                user.is_active = True
                user.email_active_code = None
                user.save()
                messages.success(request, 'ثبت‌نام شما با موفقیت انجام شد.')
                del request.session['pending_user']
                return redirect('login_page')
            else:
                form.add_error('otp', 'کد تایید وارد شده صحیح نمی‌باشد.')

        return render(request, 'account_module/otp_verify.html', {'form': form})


class LoginPageView(View):
    def get(self, request):
        login_form = LoginForm()
        return render(request, 'account_module/login.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            phone = login_form.cleaned_data.get('phone')
            password = login_form.cleaned_data.get('password')

            user = authenticate(request, username=phone, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'با موفقیت وارد شدید.')
                return redirect('index_page_urls')  # or dashboard or profile page
            else:
                login_form.add_error('phone', 'اطلاعات وارد شده صحیح نمی‌باشد.')

        return render(request, 'account_module/login.html', {'login_form': login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'با موفقیت خارج شدید.')
        return redirect('index_page_urls')  # Or any page you want after logout (like home)


class ForgetPasswordView(View):
    def get(self, request):
        forget_pass_form = ForgetPasswordForm()
        return render(request, 'account_module/forgot_password.html', {'forget_pass_form': forget_pass_form})

    def post(self, request):
        forget_pass_form = ForgetPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_phone = forget_pass_form.cleaned_data.get('phone')
            
            # Check if user exists
            user = User.objects.filter(mobile__iexact=user_phone).first()
            
            if not user:
                forget_pass_form.add_error('phone', 'کاربری با این شماره موبایل یافت نشد.')
            else:
                # Generate OTP code
                otp_code = generate_otp_code()
                user.email_active_code = otp_code
                user.save()
                
                # Send SMS
                sms_result = send_reset_password_sms(user_phone, otp_code)
                
                if sms_result['success']:
                    # Save phone in session for verification
                    request.session['reset_password_phone'] = user_phone
                    messages.success(request, 'کد تایید به شماره موبایل شما ارسال شد.')
                    return redirect('verification_reset_password_page')
                else:
                    messages.error(request, sms_result['message'])
        
        return render(request, 'account_module/forgot_password.html', {'forget_pass_form': forget_pass_form})


class VerificationResetPasswordView(View):
    def get(self, request):
        phone = request.session.get('reset_password_phone')
        if not phone:
            messages.error(request, 'لطفاً ابتدا شماره موبایل خود را وارد کنید.')
            return redirect('forget_password_page')
        
        form = OTPVerificationForm()
        return render(request, 'account_module/vertification_reset_password.html', {'verify_form': form})

    def post(self, request):
        form = OTPVerificationForm(request.POST)
        phone = request.session.get('reset_password_phone')
        
        if not phone:
            messages.error(request, 'لطفاً ابتدا شماره موبایل خود را وارد کنید.')
            return redirect('forget_password_page')
        
        user = User.objects.filter(mobile=phone).first()
        
        if not user:
            messages.error(request, 'کاربری برای تایید یافت نشد.')
            return redirect('forget_password_page')

        if form.is_valid():
            otp = form.cleaned_data.get('otp')
            if str(user.email_active_code) == str(otp):
                # Save phone in session for password reset
                request.session['reset_password_phone'] = phone
                messages.success(request, 'کد تایید صحیح است. لطفاً کلمه عبور جدید را وارد کنید.')
                return redirect('reset_password_page')
            else:
                form.add_error('otp', 'کد تایید وارد شده صحیح نمی‌باشد.')

        return render(request, 'account_module/vertification_reset_password.html', {'verify_form': form})


class ResetPasswordView(View):
    def get(self, request):
        phone = request.session.get('reset_password_phone')
        if not phone:
            messages.error(request, 'لطفاً ابتدا کد تایید را وارد کنید.')
            return redirect('forget_password_page')
        
        form = ResetPasswordForm()
        return render(request, 'account_module/reset_password.html', {'form': form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        phone = request.session.get('reset_password_phone')
        
        if not phone:
            messages.error(request, 'لطفاً ابتدا کد تایید را وارد کنید.')
            return redirect('forget_password_page')
        
        user = User.objects.filter(mobile=phone).first()
        
        if not user:
            messages.error(request, 'کاربری یافت نشد.')
            return redirect('forget_password_page')

        if form.is_valid():
            new_password = form.cleaned_data.get('password')
            user.set_password(new_password)
            user.email_active_code = None  # Clear the OTP code
            user.save()
            
            # Clear session
            del request.session['reset_password_phone']
            
            messages.success(request, 'کلمه عبور شما با موفقیت تغییر یافت. لطفاً وارد شوید.')
            return redirect('login_page')

        return render(request, 'account_module/reset_password.html', {'form': form})