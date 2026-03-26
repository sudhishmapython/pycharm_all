
import io
import uuid
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from django.core.files.base import ContentFile
from .models import CertificateTemplate
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont




def generate_certificate_pdf(data):
    pdfmetrics.registerFont(TTFont('TimesNewRoman', 'C:\\Windows\\Fonts\\times.ttf'))
    pdfmetrics.registerFont(TTFont('TimesNewRoman-Bold', 'C:\\Windows\\Fonts\\timesbd.ttf'))

    packet = io.BytesIO()
    can = canvas.Canvas(packet)

    # 🔥 DATE CONVERSION
    from_date = data.get('from_date')
    to_date = data.get('to_date')
    issue_date = data.get('issue_date')

    from_date = from_date.strftime("%d-%m-%Y") if from_date else ""
    to_date = to_date.strftime("%d-%m-%Y") if to_date else ""
    issue_date = issue_date.strftime("%d-%m-%Y") if issue_date else ""

    certificate_id = data.get('certificate_id', '')

    page_width = 595

    # ================================
    # 🔥 NAME
    # ================================
    can.setFont("TimesNewRoman-Bold", 20)
    name = str(data.get('student_name', ''))
    name_width = can.stringWidth(name, "TimesNewRoman-Bold", 20)
    can.drawString((page_width - name_width) / 2, 404, name)

    # ================================
    # 🔥 COURSE
    # ================================
    can.setFont("TimesNewRoman", 14)
    course = str(data.get('course', ''))
    course_width = can.stringWidth(course, "TimesNewRoman", 14)
    can.drawString((page_width - course_width) / 2, 320, course)

    # ================================
    # 🔥 PERFORMANCE
    # ================================
    can.setFont("TimesNewRoman", 14)
    performance = str(data.get('performance', ''))
    perf_width = can.stringWidth(performance, "TimesNewRoman", 14)
    can.drawString(350, 252, performance)

    # ================================
    # 🔥 FROM - TO DATE
    # ================================
    can.setFont("TimesNewRoman", 12)
    can.drawString(79, 296, from_date)
    can.drawString(190, 296, to_date)

    # ================================
    # 🔥 ISSUE DATE
    # ================================
    can.drawString(460, 784, issue_date)

    # ================================
    # 🔥 CERTIFICATE ID
    # ================================
    can.setFont("TimesNewRoman", 12)
    can.drawString(143, 783, certificate_id)

    can.save()

    # ================================
    # 🔥 MERGE WITH TEMPLATE
    # ================================
    packet.seek(0)
    new_pdf = PdfReader(packet)

    template_obj = CertificateTemplate.objects.filter(pinned=True).first()

    if not template_obj:
        raise Exception("No template uploaded")

    template = PdfReader(template_obj.template_file.path)
    page = template.pages[0]

    page.merge_page(new_pdf.pages[0])

    writer = PdfWriter()
    writer.add_page(page)

    output = io.BytesIO()
    writer.write(output)

    file_name = f"{uuid.uuid4()}.pdf"
    return file_name, ContentFile(output.getvalue())