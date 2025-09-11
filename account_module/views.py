import sys
import io
import random

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.urls import reverse

from account_module.forms import RegisterFormSecond, OTPVerificationForm, LoginForm
from account_module.models import User
from kavenegar import KavenegarAPI, APIException, HTTPException

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
            token = random.randint(100000, 999999)  # 6 digit OTP code
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

                try:
                    api = KavenegarAPI('316A6A486777346739666B5868655269564E6C39644B396249566E705070374A6A7854686879394A746C493D')
                    params = {
                        'receptor': user_phone,
                        'template': 'Activation',  # <-- Use your own template name here
                        'token': token,
                        'type': 'sms',  # sms or call
                    }
                    response = api.verify_lookup(params)
                    print("Kavenegar verify_lookup response:", response)

                except APIException as e:
                    print(f"Kavenegar APIException: {str(e)}")
                    messages.error(request, 'مشکلی در ارسال کد تایید به وجود آمد، لطفاً دوباره تلاش کنید.')
                    new_user.delete()
                    return render(request, 'account_module/register.html', {'register_form': register_form})

                except HTTPException as e:
                    print(f"Kavenegar HTTPException: {str(e)}")
                    messages.error(request, 'مشکلی در ارسال کد تایید به وجود آمد، لطفاً دوباره تلاش کنید.')
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