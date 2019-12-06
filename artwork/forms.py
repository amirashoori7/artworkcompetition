from django import forms
from .models import Artwork

class EntryForm(forms.ModelForm):
    #to tell django which model to use to create this form
    class Meta:
        model = Artwork
        fields = ['worktitle', 'surname', 'firstname',
                  'school', 'workfile', 'email',
                  'dob', 'parentname', 'parentemail',
                  'parentphone', 'learnergrade', 'teachername',
                  'teacheremail', 'teacherphone', 'testimonial',
                  'question1', 'question2', 'question3']
