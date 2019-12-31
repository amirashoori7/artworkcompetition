from django import forms
from .models import Artwork, School
from _overlapped import NULL


class EntryForm(forms.ModelForm):

#     schools = forms.ModelChoiceField(
#         queryset=School.objects.all(),
#         to_field_name="name"
#     )
    # to tell django which model to use to create this form
    class Meta:
        model = Artwork
        # fields = '__all__'
        fields = ['worktitle', 'surname', 'firstname',
                  'school', 'workfile', 'email',
                  'dob', 'parentname', 'parentemail',
                  'parentphone', 'learnergrade', 'teachername',
                  'teacheremail', 'teacherphone', 'cellphone',
                  'question1', 'question2', 'question3']

    
#     def handle_uploaded_file(self, f):
# #         .FILES['file']
#         with open('some/file/name.txt', 'wb+') as destination:
#                 for chunk in f.chunks():
#                     destination.write(chunk)
#         return NULL
        


