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
    parentphone = forms.CharField(error_messages={'required': 'Please enter your parent\'s phone number'})
    username = forms.EmailField(error_messages={'required': 'Please enter a valid email address'}, validators=default_validators)
    dob = forms.DateField(error_messages={'required': 'Please enter your birth date'})
    cellphone = forms.CharField(error_messages={'required': 'Please enter a 10-digits cell phone number'}, max_length = 10, min_length=10)
 
    class Meta:
        model = ProjectUser
        fields = ('username', 'first_name', 'last_name', 'parentname', 'dob', 'parentphone', 'password1', 'password2', 'cellphone')


class AdvancedUserRegistrationForm(UserCreationForm):
    username_validator = UnicodeUsernameValidator()
    default_validators = [username_validator]
    first_name = forms.CharField(error_messages={'required': 'Please enter the name'})
    last_name = forms.CharField(error_messages={'required': 'Please enter last name'})
    organisation = forms.CharField(error_messages={'required': 'Please enter the organisation name'})
    username = forms.EmailField(error_messages={'required': 'Please enter a valid email address'}, validators=default_validators)
    dob = forms.DateField(error_messages={'required': 'Please enter your birth date'})
 
    class Meta:
        model = ProjectUser
        fields = ('username', 'first_name', 'last_name', 'dob', 'user_type', 'organisation', 'password1', 'password2', 'cellphone')


# 1- learner phone (compulsory)
# 2- learner email  (compulsory)
# 3- parent email (optional)
# 4- parent phone (compulsory)
# 5- teacher email (compulsory )
# 6- teacher phone (optional)