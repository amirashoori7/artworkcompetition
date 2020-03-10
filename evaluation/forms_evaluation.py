from django import forms
from evaluation.models import D1A, D2, D1B

class FormD1A(forms.ModelForm):
    class Meta:
        model = D1A
        fields = ['imgq', 'answersq', 'originq', 'id']

class FormD1B(forms.ModelForm):
    class Meta:
        model = D1B
        fields = ['comment', 'id', 'workis']
        
class FormD2(forms.ModelForm):
    class Meta:
        model = D2
        fields = ['math', 'q1', 'q2', 'q3', 'q4']


class FormD3(forms.ModelForm):
    class Meta:
        model = D2
        fields = ['math', 'q1', 'q2', 'q3', 'q4', 'score', 'comment', 'author']