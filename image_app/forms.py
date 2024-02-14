from django import forms
from django.contrib.auth.models import User
from .models import Image


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email Address'})
        }
        help_texts = {
            'username': None,
            'password': None,
            'first_name': None
        }


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
