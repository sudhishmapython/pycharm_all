from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import RadioSelect

from demoapp.models import Student, Studentimage, SutudRadio

YEAR_CHOICES = [(str(year), str(year)) for year in range(2023, 1990, -1)]

class StudentForm(forms.ModelForm):
    class Meta:
        model=Studentimage
        fields='__all__'





class RadioForm(forms.ModelForm):
    year_of_passout = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(
        attrs={'class': 'year-dropdown'}))
    gender = forms.ChoiceField(widget=RadioSelect,
                                           choices=[('male', 'male'), ('female', 'female')])

    class Meta:
        model = SutudRadio
        fields = ('name', 'year_of_passout','gender')