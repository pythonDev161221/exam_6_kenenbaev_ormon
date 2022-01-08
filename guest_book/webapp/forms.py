from django import forms

from .models import STATUSCHOICES


class CustomerForm(forms.Form):
    customer_name = forms.CharField(max_length=100, required=True, label="Имя")
    customer_email = forms.EmailField(max_length=254, required=True, label="Email")
    order_text = forms.CharField(max_length=2000, required=True, widget=forms.Textarea, label="Текст")
