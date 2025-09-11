from django import forms
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.exceptions import ValidationError

from account_module.models import User


class RegisterFormSecond(forms.Form):
    phone = forms.CharField(
        label='شماره موبایل',
        widget=forms.NumberInput(
            attrs={'placeholder': ' شماره موبایل خود را وارد کنید  ', 'class': 'form-control text-center mt-4 mb-3'}
        )
    )
    password = forms.CharField(
        label='کلمه عبور جدید ',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'کلمه عبور  ', 'class': 'form-control text-center mt-4 mb-3'}
        ),
        validators=[validators.MaxLengthValidator(100)]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور جدید',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'تکرار کلمه عبور  ', 'class': 'form-control text-center mt-4 mb-3'}
        ),
        validators=[validators.MaxLengthValidator(100)]
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')

        return cleaned_data

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


class VertificationForm(forms.Form):

    vertification = forms.CharField(
        label='کد تایید: ',
        widget=forms.PasswordInput(attrs={'placeholder': 'کد تایید پیامک شده را وارد کنید  ', 'class': 'form-control '
                                                                                                       'text-center '
                                                                                                       'mt-4 mb-3'}))


class LoginForm(forms.Form):
    phone = forms.CharField(
        label='شماره موبایل',
        widget=forms.NumberInput(
            attrs={'placeholder': 'شماره موبایل خود را وارد کنید', 'class': 'form-control text-center mt-4 mb-3'}
        ),
        validators=[
            validators.MaxLengthValidator(11),
            validators.MinLengthValidator(11),
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'کلمه عبور', 'class': 'form-control text-center mt-4 mb-3'}
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not User.objects.filter(mobile=phone, is_active=True).exists():
            raise ValidationError('کاربری با این شماره موبایل یافت نشد یا حساب فعال نشده است.')
        return phone

    password = forms.CharField(
        label='کلمه عبور ',
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور  ', 'class': 'form-control text-center mt-4 mb-3'}),
        validators=[
            validators.MaxLengthValidator(100),

        ]
    )


class ForgetPasswordForm(forms.Form):
    phone = forms.CharField(
        label='شماره موبایل',
        widget=forms.NumberInput(
            attrs={'placeholder': ' شماره موبایل خود را وارد کنید  ', 'class': 'form-control text-center mt-4 mb-3'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='کلمه عبور جدید ',
        widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور  ', 'class': 'form-control text-center mt-4 mb-3'}),
        validators=[
            validators.MaxLengthValidator(100),

        ]
    )

    confirm_password = forms.CharField(
        label='تکرار کلمه عبور  جدید',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'تکرار کلمه عبور  ', 'class': 'form-control text-center mt-4 mb-3'}),
        validators=[
            validators.MaxLengthValidator(100),

        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


class OTPVerificationForm(forms.Form):
    otp = forms.CharField(label='کد تایید: ',
        widget=forms.PasswordInput(attrs={'placeholder': 'کد تایید پیامک شده را وارد کنید  ', 'class': 'form-control '
                                                                                                       'text-center '
                                                                                                       'mt-5 mb-3'}))
class UserRegisterInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'postal_code', 'mobile']
        labels = {
            'first_name': ':نام',
            'last_name': ':نام خانوادگی',
            'address': ':آدرس',
            'mobile': ':شماره موبایل',
            'postal_code': 'کدپستی',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control text-right'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control text-right'}),
            'address': forms.Textarea(attrs={'class': 'form-control text-right', 'rows': 3}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control text-right', 'rows': 3}),
            'mobile': forms.TextInput(attrs={'class': 'form-control text-right yekan-font'}),
        }

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'check_purchase_credit': 'اعتبار خرید چکی (تومان)',
            'has_check_purchase_permission': 'دارای مجوز خرید چکی؟',
        }
        widgets = {
            'check_purchase_credit': forms.NumberInput(attrs={
                'class': 'form-control text-center',
                'style': 'width: 150px; font-size: 16px; padding: 5px;',  # bigger width and font size
                'min': '0'  # optional, for number input min value
            }),
            'has_check_purchase_permission': forms.CheckboxInput(attrs={
                'style': 'transform: scale(1.3); margin-left: 10px;'  # bigger checkbox if you want
            }),
        }