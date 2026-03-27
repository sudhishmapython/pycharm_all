from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CertificateForm, TemplateForm
from .models import Certificate
from datetime import datetime
from .utils import generate_certificate_pdf_preview, generate_certificate_pdf
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
    # 🔥 session-il already data undo?
    session_data = request.session.get('cert_data')

    # 👉 IF GET request (Edit click vannal)
    if request.method == "GET" and session_data:
        form = CertificateForm(initial=session_data)

    else:
        form = CertificateForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        last_cert = Certificate.objects.order_by('-id').first()

        if last_cert and last_cert.certificate_id.startswith('FL'):
            last_number = int(last_cert.certificate_id.replace('FL', ''))
            new_number = last_number + 1
        else:
            new_number = 1

        certificate_id = f"FL{new_number:02d}"

        # 🔥 session save
        request.session['cert_data'] = {
            'student_name': form.cleaned_data['student_name'],
            'course': form.cleaned_data['course'],
            'from_date': str(form.cleaned_data['from_date']),
            'to_date': str(form.cleaned_data['to_date']),
            'performance': form.cleaned_data['performance'],
            'issue_date': str(form.cleaned_data['issue_date']),
            'certificate_id': certificate_id
        }

        return redirect('preview_certificate')

    return render(request, 'generate.html', {'form': form})


def preview_certificate(request):
    return render(request, 'preview.html')



def preview_pdf(request):
    data = request.session.get('cert_data')

    if not data:
        return redirect('generate')

    data['from_date'] = datetime.strptime(data['from_date'], "%Y-%m-%d")
    data['to_date'] = datetime.strptime(data['to_date'], "%Y-%m-%d")
    data['issue_date'] = datetime.strptime(data['issue_date'], "%Y-%m-%d")

    pdf = generate_certificate_pdf_preview(data)

    return HttpResponse(pdf, content_type='application/pdf')


def confirm_certificate(request):
    data = request.session.get('cert_data')

    if not data:
        return redirect('generate')

    from datetime import datetime

    data['from_date'] = datetime.strptime(data['from_date'], "%Y-%m-%d")
    data['to_date'] = datetime.strptime(data['to_date'], "%Y-%m-%d")
    data['issue_date'] = datetime.strptime(data['issue_date'], "%Y-%m-%d")

    cert = Certificate()
    cert.student_name = data['student_name']
    cert.course = data['course']
    cert.issue_date = data['issue_date']
    cert.certificate_id = data['certificate_id']

    file_name, pdf_file = generate_certificate_pdf(data)

    cert.pdf_file.save(file_name, pdf_file)
    cert.save()

    del request.session['cert_data']

    return redirect('verify')


def verify_certificate(request):
    if request.method == "POST":
        cert_id = request.POST.get('certificate_id')

        try:
            cert = Certificate.objects.get(certificate_id=cert_id)

            return render(request, 'verify.html', {
                'pdf_url': cert.pdf_file.url
            })

        except Certificate.DoesNotExist:
            return render(request, 'verify.html', {
                'error': 'Invalid Certificate'
            })

    return render(request, 'verify.html')