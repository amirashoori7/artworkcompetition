from . import models
from django import forms

class FormD1A(forms.ModelForm):
    class Meta:
        model = EvalD1A
        fields = ['biodetails', 'picview', 'paragraphsview', 'comment']
