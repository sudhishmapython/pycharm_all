from django import forms

from demoapp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('name','price')
