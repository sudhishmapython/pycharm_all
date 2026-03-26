from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CertificateForm, TemplateForm
from .models import Certificate
from .utils import generate_certificate_pdf
import uuid

# LOGIN
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('dashboard')
        return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def add_template(request):
    form = TemplateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'add_template.html', {'form': form})


@login_required
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
            'issue_date': cert.issue_date,
            'certificate_id': cert.certificate_id
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
        except:
            return render(request, 'result.html', {'error': 'Invalid Certificate'})

    return render(request, 'verify.html')