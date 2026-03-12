from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Student(models.Model):
    name=models.CharField(max_length=200)
    mark=models.IntegerField()
    place=models.CharField(max_length=200)


class Studentimage(models.Model):
    name=models.CharField(max_length=200)
    mark=models.IntegerField()
    place=models.CharField(max_length=200)
    image = models.FileField(upload_to='uploads/')





class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    description=models.CharField(max_length=250)







class SutudRadio(models.Model):
    name=models.CharField(max_length=250)
    gender = models.CharField(max_length=250, null=True, blank=True)
    year_of_passout = models.CharField(max_length=250, null=True, blank=True)




class Login(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)


class Nurse(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='nurse')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)



class Customer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='nurse')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(max_length=200)