from django.db import models

# Create your models here.
class Student(models.Model):
    stud_id=models.IntegerField()
    name=models.CharField(max_length=250)
    status=models.CharField(max_length=250)

