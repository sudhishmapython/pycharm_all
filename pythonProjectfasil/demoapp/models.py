from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    description=models.CharField(max_length=250)

class Student(models.Model):
    name=models.CharField(max_length=250)
    mark=models.IntegerField()
    place=models.CharField(max_length=250)

class College(models.Model):
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    image=models.FileField(upload_to='uploads/')



class Login(AbstractUser):
    is_nurse=models.BooleanField(default=False)
    is_user=models.BooleanField(default=True)


class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250)

class Nurse(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='nurse')
    name = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    qualification=models.CharField(max_length=250)
    experience=models.CharField(max_length=250)