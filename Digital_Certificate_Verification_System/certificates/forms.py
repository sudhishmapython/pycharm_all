from django import forms
from .models import Certificate, CertificateTemplate

class CertificateForm(forms.ModelForm):
    from_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    to_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    issue_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    performance = forms.CharField()

    class Meta:
        model = Certificate
        fields = ['student_name', 'course', 'issue_date']


class TemplateForm(forms.ModelForm):
    class Meta:
        model = CertificateTemplate
        fields = ['name', 'template_file', 'pinned']