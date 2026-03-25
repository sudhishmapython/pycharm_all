from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    # 🔥 EXTRA FIELDS (model-il illa)
    from_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    issue_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    performance = forms.CharField(max_length=50)

    class Meta:
        model = Certificate
        fields = ['student_name', 'course', 'duration', 'issue_date']