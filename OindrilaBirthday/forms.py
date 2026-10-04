# forms.py
from django import forms

class BirthdayWishForm(forms.Form):
    guest_name = forms.CharField(
        max_length=100,
        label="Whom You want to Dedicate: ",
        widget=forms.TextInput(attrs={
            'placeholder': 'E.g. Rahul',
            'class': 'form-input'
        })
    )
    note = forms.CharField(
        label="Thank you Note: ",
        widget=forms.Textarea(attrs={
            'placeholder': 'Write something sweet...',
            'rows': 4,
            'class': 'form-input'
        })
    )