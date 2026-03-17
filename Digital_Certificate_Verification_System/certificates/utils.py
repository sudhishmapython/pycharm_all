import io
import uuid
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from django.core.files.base import ContentFile
from .models import CertificateTemplate

def generate_certificate_pdf(data):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    # 🔥 SAFE DATE CONVERSION (IMPORTANT)
    from_date = data.get('from_date')
    to_date = data.get('to_date')
    issue_date = data.get('issue_date')

    from_date = from_date.strftime("%d-%m-%Y") if from_date else ""
    to_date = to_date.strftime("%d-%m-%Y") if to_date else ""
    issue_date = issue_date.strftime("%d-%m-%Y") if issue_date else ""

    # 🔥 TEXT DRAWING
    # 🔥 NAME (meenakshi position)
    can.setFont("Helvetica-Bold", 26)
    can.drawString(207, 412, str(data.get('student_name', '')))

    # 🔥 COURSE (PYTHON DJANGO position)
    can.setFont("Helvetica-Bold", 18)
    can.drawString(230, 460, str(data.get('course', '')))

    # 🔥 FROM - TO DATE
    can.setFont("Helvetica", 14)
    can.drawString(200, 420, from_date)  # from date
    can.drawString(350, 420, to_date)  # to date

    # 🔥 PERFORMANCE
    can.setFont("Helvetica-Bold", 16)
    can.drawString(250, 380, str(data.get('performance', '')))

    can.save()

    packet.seek(0)
    new_pdf = PdfReader(packet)

    # 🔥 GET TEMPLATE FROM ADMIN
    template_obj = CertificateTemplate.objects.filter(pinned=True).first()

    if not template_obj:
        raise Exception("No template uploaded")

    template = PdfReader(template_obj.template_file.path)
    page = template.pages[0]

    # 🔥 MERGE TEXT WITH TEMPLATE
    page.merge_page(new_pdf.pages[0])

    writer = PdfWriter()
    writer.add_page(page)

    output = io.BytesIO()
    writer.write(output)

    file_name = f"{uuid.uuid4()}.pdf"
    return file_name, ContentFile(output.getvalue())