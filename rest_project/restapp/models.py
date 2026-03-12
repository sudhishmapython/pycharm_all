from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250)
    discription=models.TextField()


# class Cake(models.Model):
#     category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="cakes")
#     name=models.CharField(max_length=250)
#     discription=models.CharField(max_length=250)
#     price=models.IntegerField()
#     stock=models.IntegerField(default=0)
#     image=models.FileField(upload_to='uploads/')