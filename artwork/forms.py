from django import forms
from .models import Artwork, School

class EntryForm(forms.ModelForm):

    class Meta:
        model = Artwork
        # fields = '__all__'
        fields = ['worktitle', 'surname', 'firstname', 'id',
                  'school', 'workfile', 'email',
                  'dob', 'parentname', 'parentemail',
                  'parentphone', 'learnergrade', 'teachername',
                  'teacheremail', 'teacherphone', 'cellphone',
                  'question1', 'question2', 'question3']
