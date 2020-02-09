from django.contrib.auth.forms import UserCreationForm
from django import forms
from account.models_account import ProjectUser
from django.contrib.auth.validators import UnicodeUsernameValidator


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    username_validator = UnicodeUsernameValidator()
    default_validators = [username_validator]
    
    first_name = forms.CharField(error_messages={'required': 'Please enter your name'})
    last_name = forms.CharField(error_messages={'required': 'Please enter your last name'})
    parentname = forms.CharField(error_messages={'required': 'Please enter your parent\'s full-name'})
    parentemail = forms.EmailField(error_messages={'required': 'Please enter your parent\'s email address'})
    parentphone = forms.CharField(error_messages={'required': 'Please enter your parent\'s cell phone number'})
    username = forms.EmailField(error_messages={'required': 'Please enter a valid email address'}, validators=default_validators)
    dob = forms.DateField(error_messages={'required': 'Please enter your birth date'})
 
    class Meta:
        model = ProjectUser
        fields = ('username', 'first_name', 'last_name', 'parentname', 'parentphone', 'dob', 'parentemail', 'password1', 'password2', 'cellphone')
