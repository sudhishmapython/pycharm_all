from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    description=models.CharField(max_length=250)


class Student(models.Model):
    name=models.CharField(max_length=300)
    mark=models.IntegerField()
    colllege=models.CharField(max_length=300)

class Student1(models.Model):
    name=models.CharField(max_length=300)
    mark=models.IntegerField()
    course=models.CharField(max_length=300)
    
    
class Demotable(models.Model):
    name=models.CharField(max_length=300)
    price=models.IntegerField()
    description=models.CharField(max_length=300)