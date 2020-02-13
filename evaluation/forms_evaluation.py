from django import forms
from evaluation.models import D1A, D2

class FormD1A(forms.ModelForm):
    class Meta:
        model = D1A
        fields = ['artwork', 'imgq', 'answersq', 'originq', 'revisit', 'comment', 'author']


class FormD2(forms.ModelForm):
    class Meta:
        model = D2
        fields = ['math', 'q1', 'q2', 'q3', 'q4', 'score', 'comment', 'author']


