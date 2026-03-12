from django.db import models

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.IntegerField()
    size=models.IntegerField()

class Student(models.Model):
    name=models.CharField(max_length=250)
    course=models.CharField(max_length=250)
    mark=models.IntegerField()
    image = models.FileField(upload_to='uploads/')

class Image(models.Model):
    pic = models.FileField(upload_to='MiniApp_Images')


# class Image(models.Model):
#     image=models.FileField(upload_to='uploads/')
