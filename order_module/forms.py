from django import forms
from .models import Payment

class PaymentForm(forms.Form):
    amount = forms.IntegerField(
        label='مبلغ پرداخت (ریال)',
        min_value=1000,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'مبلغ را به ریال وارد کنید',
            'min': '1000'
        })
    )
    description = forms.CharField(
        label='توضیحات پرداخت',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'توضیحات اختیاری برای پرداخت',
            'rows': 3
        })
    )

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount and amount < 1000:
            raise forms.ValidationError('حداقل مبلغ پرداخت 1000 ریال می‌باشد.')
        return amount
