from django.db import models

class Certificate(models.Model):

    student_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    certificate_id = models.CharField(max_length=50, unique=True)
    issue_date = models.DateField()

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('verified', 'Verified'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.student_name