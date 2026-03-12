from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=250)
    place=models.CharField(max_length=250)


class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    discription=models.CharField(max_length=250)

class Employee(models.Model):
    name=models.CharField(max_length=250)
    job=models.CharField(max_length=250)
    salary=models.IntegerField()
