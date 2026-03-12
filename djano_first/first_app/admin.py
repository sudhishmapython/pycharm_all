from django.contrib import admin
from first_app import models
from first_app.models import Student,Image


# Register your models here.


# admin.site.register(models.Student)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'mark', 'image')


admin.site.register(Student, ProductAdmin)
admin.site.register(Image)
