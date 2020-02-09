from django import forms
from evaluation.models import D1A

class FormD1A(forms.ModelForm):
    class Meta:
        model = D1A
        fields = ['artwork', 'imgq', 'answersq', 'originq', 'revisit', 'comment', 'author']
