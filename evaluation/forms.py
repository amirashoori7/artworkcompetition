from . import models
from django import forms

class FormD1A(forms.ModelForm):
    class Meta:
        model = D1A
        fields = ['artwork', 'imgq', 'answersq', 'originq', 'revisit', 'comment', 'author']
