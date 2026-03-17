from django.db import models


class CertificateTemplate(models.Model):
    name = models.CharField(max_length=100)
    template_file = models.FileField(upload_to="templates/")
    pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Certificate(models.Model):
    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    issue_date = models.DateField()
    certificate_id = models.CharField(max_length=50, unique=True)
    pdf_file = models.FileField(upload_to="certificates/")

    def __str__(self):
        return self.certificate_id
