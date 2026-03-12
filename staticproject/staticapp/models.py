from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_physician = models.BooleanField(default=False)
    gender = models.CharField(max_length=50,null=True)
    phone_no = models.IntegerField(null=True, blank=True)
    occupation = models.CharField(max_length=50,null=True)
    image=models.FileField(upload_to ='uploads/')
