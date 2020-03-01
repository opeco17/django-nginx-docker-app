from django import forms
from django.core import validators


class NameForm(forms.Form):
    name = forms.CharField(
        label=False,
        required=True,
        max_length=30,
        validators=[validators.MaxLengthValidator(30)],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
    )
