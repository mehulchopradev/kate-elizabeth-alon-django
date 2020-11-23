from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter user'
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }))