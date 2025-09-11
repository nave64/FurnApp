from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account_module.models import User

forms_error_messages = {
    'required': 'لطفا این فیلد را پر کنید '
}


class EditProfileModelForm(forms.ModelForm):
    first_name = forms.CharField(label=':نام ',required=True, widget=forms.TextInput(attrs={'class': 'form-control text-right'}))
    last_name = forms.CharField(label=':نام خانوادگی ',required=True, widget=forms.TextInput(attrs={'class': 'form-control text-right'}))
    address = forms.CharField(label=':آدرس ',required=True,
                              widget=forms.Textarea(attrs={'class': 'form-control text-right', 'rows': 3}))
    postal_code = forms.CharField(label=':کد پستی ',required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control text-right', 'rows': 3}))
    mobile = forms.CharField(label=':شماره موبایل ',required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control text-right yekan-font'}))

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


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label=':کلمه عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    password = forms.CharField(
        label=':کلمه عبور جدید',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    confirm_password = forms.CharField(
        label=':تکرار کلمه عبور جدید',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')


# forms.py

from django import forms
from .models import UserImageUpload

MAX_IMAGE_SIZE_MB = 2

class UserImageUploadForm(forms.ModelForm):
    class Meta:
        model = UserImageUpload
        fields = ['image_1', 'image_2']
        labels = {
            'image_1': 'تصویر اول (الزامی)',
            'image_2': 'تصویر دوم (اختیاری)',
        }
        widgets = {
            'image_1': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'فایل تصویر اول را انتخاب کنید'
            }),
            'image_2': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'فایل تصویر دوم را انتخاب کنید (اختیاری)'
            }),
        }

    # ✅ Make image_2 optional
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image_2'].required = False

    # ✅ Validation for size limit
    def clean_image_1(self):
        image = self.cleaned_data.get('image_1')
        if image and image.size > MAX_IMAGE_SIZE_MB * 1024 * 1024:
            raise forms.ValidationError(f"تصویر اول نباید بیشتر از {MAX_IMAGE_SIZE_MB} مگابایت باشد.")
        return image

    def clean_image_2(self):
        image = self.cleaned_data.get('image_2')
        if image and image.size > MAX_IMAGE_SIZE_MB * 1024 * 1024:
            raise forms.ValidationError(f"تصویر دوم نباید بیشتر از {MAX_IMAGE_SIZE_MB} مگابایت باشد.")
        return image

