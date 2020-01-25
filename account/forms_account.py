from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models_account import ProjectUser

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = ProjectUser
        fields = ('username', 'email', 'password1', 'password2', 'last_name', 'first_name')
