from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import CertificateForm
from .models import Certificate, CertificateTemplate
from .utils import generate_certificate_pdf
import uuid

def generate_certificate(request):
    form = CertificateForm(request.POST or None)

    if form.is_valid():
        cert = form.save(commit=False)

        cert.certificate_id = "CERT-" + str(uuid.uuid4())[:8]

        data = {
            'student_name': cert.student_name,
            'course': cert.course,
            'from_date': form.cleaned_data['from_date'],
            'to_date': form.cleaned_data['to_date'],
            'performance': form.cleaned_data['performance'],
            'certificate_id': cert.certificate_id,
            'issue_date': cert.issue_date
        }

        file_name, pdf_file = generate_certificate_pdf(data)
        cert.pdf_file.save(file_name, pdf_file)

        cert.save()
        return redirect('verify')

    return render(request, 'generate.html', {'form': form})


def verify_certificate(request):
    if request.method == "POST":
        cert_id = request.POST.get('certificate_id')

        try:
            cert = Certificate.objects.get(certificate_id=cert_id)
            return render(request, 'result.html', {'cert': cert})
        except Certificate.DoesNotExist:
            return render(request, 'result.html', {'error': 'Invalid Certificate'})

    return render(request, 'verify.html')
