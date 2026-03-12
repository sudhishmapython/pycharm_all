import django_filters
from django import forms
from django_filters import CharFilter, filters
from Futura_App.models import Trainer,Student


# class StudentFilter(django_filters.FilterSet):
#     name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
#                   'placeholder': 'Search Name', 'class': 'form-control'}))
#
#     class Meta:
#         model = Person
#         fields = ('name',)


class TrainerFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
                  'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = Trainer
        fields = ('name',)


