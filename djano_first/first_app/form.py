from django import forms
from .models import Student, Product,Image


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'




class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'


class ImagesForm(forms.ModelForm):
    pic = forms.FileField(widget = forms.TextInput(attrs={
            "name": "images",
            "type": "File",
            "class": "form-control",
            "multiple": "True",
        }), label = "")
    class Meta:
        model = Image
        fields = ['pic']




# class ImageForm(ModelForm):
#     class Meta:
#         model=Image
#         fields='__all__'