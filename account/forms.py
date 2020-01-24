from . models import ProjectUser
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = ProjectUser
        fields = ('username', 'email', 'password1', 'password2')
