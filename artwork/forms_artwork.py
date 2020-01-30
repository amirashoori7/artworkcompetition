from django import forms
from .models_artwork import Artwork
from account.models_account import ProjectUser

class EntryForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['worktitle', 'id', 'school', 'workfile', 'workfileCropped',
                  'learnergrade', 'workformulafile','teachername',
                  'teacheremail', 'teacherphone', 'question1',
                  'question2', 'question3']


class UserForm(forms.ModelForm):
    class Meta:
        model = ProjectUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'dob', 'cellphone', 'parentname', 'parentemail',
                  'parentphone')
