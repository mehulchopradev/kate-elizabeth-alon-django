from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter user'
    }))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }))

''' class RegisterForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={
        'placeholder': 'Enter username'
    }))
    password = forms.IntegerField(label='', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password'
    }))
    country = forms.ChoiceField(label='Country: ', choices=(('IN', 'India'), ('USA', 'United states of america'), ('AU', 'Australia')))
    gender = forms.ChoiceField(label='Gender: ', choices=(('M', 'Male'), ('F', 'Female')), widget=forms.RadioSelect(attrs={
        'class': 'inline'
    })) '''

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'country', 'gender', 'profile_pic')

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Enter username'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Enter password'
            }),
        }

        labels = {
            'username': '',
            'password': '',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # database code over here to get the countries from the backend

        self.fields['gender'] = forms.ChoiceField(label='Gender: ', choices=(('M', 'Male'), ('F', 'Female')),\
            widget=forms.RadioSelect())
        self.fields['country'] = forms.ChoiceField(label='Country: ', choices=(('IN', 'India'), ('USA', 'United states of america'),\
             ('AU', 'Australia')))