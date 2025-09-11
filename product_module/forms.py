from django import forms
from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={
                'placeholder': 'نظر خود را بنویسید...',
                'rows': 4,
                'class': 'form-control'
            })
        }
        labels = {
            'text': ''
        }
