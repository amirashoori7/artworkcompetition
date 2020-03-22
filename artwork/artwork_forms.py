from django import forms
from artwork.artwork_models import Artwork
from account.models_account import ProjectUser

class EntryForm(forms.ModelForm):
    teacheremail = forms.EmailField(error_messages={'required': 'Please enter a valid email address'})
    class Meta:
        model = Artwork
        fields = ['worktitle', 'id', 'workfile', 'workfileCropped',
                  'learnergrade', 'workformulafile','teachername',
                  'teacheremail', 'question1',
                  'question2', 'question3']


class UserForm(forms.ModelForm):
    class Meta:
        model = ProjectUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'dob', 'cellphone', 'parentname', 'parentemail',
                  'parentphone')
