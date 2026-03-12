from django import forms
from django.contrib.auth.forms import UserCreationForm

from demoapp.models import Student, User, Nurse, Login


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class LoginRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, )
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput, )



    class Meta:
        model = Login
        fields = ('username', 'password1', 'password2')



class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'place')


class NurseRegister(forms.ModelForm):
    class Meta:
        model = Nurse
        fields = ('name', 'place','qualification')