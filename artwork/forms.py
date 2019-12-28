from django import forms
from .models import Artwork, School

class EntryForm(forms.ModelForm):
    school = forms.ModelChoiceField(
        queryset=School.objects.all(),
        to_field_name="name"
    )
    #to tell django which model to use to create this form
    class Meta:
        model = Artwork
        #fields = '__all__'
        fields = ['worktitle', 'surname', 'firstname',
                  'school', 'workfile', 'email',
                  'dob', 'parentname', 'parentemail',
                  'parentphone', 'learnergrade', 'teachername',
                  'teacheremail', 'teacherphone', 'testimonial',
                  'question1', 'question2', 'question3']
