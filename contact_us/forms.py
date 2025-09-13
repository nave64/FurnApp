# contact_us/forms.py
from django import forms
from django_recaptcha.fields import ReCaptchaField

from django import forms
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from contact_us.models import ContactUs

class ContactUsModelForm(forms.ModelForm):
    # Temporarily disable captcha for development
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = ContactUs
        fields = ['full_name', 'mobile', 'title', 'message']  # Removed 'captcha'
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'نام و نام خانوادگی'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'شماره موبایل'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'موضوع پیام'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'متن پیام',
                'rows': 5
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
