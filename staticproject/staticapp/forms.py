from django.contrib.auth.forms import UserCreationForm
from django import forms
from staticapp.models import User

class Customerform(UserCreationForm):
    # first_name = forms.CharField(max_length=250)
    # email = forms.EmailField(max_length=250)
    # phone_no = forms.CharField(max_length=250)
    # gender = forms.CharField(max_length=250)
    # occupation = forms.CharField(max_length=250)
    username=forms.CharField(max_length=250)
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ('first_name', 'email', 'phone_no', 'gender', 'occupation','image','username', 'password1', 'password2', )

class Physicianform(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','phone_no', 'email','username', 'password1', 'password2')
