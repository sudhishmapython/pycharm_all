from django import forms

from demoapp.models import Student1


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student1
        fields='__all__'


