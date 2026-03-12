from django.contrib import admin
from .models import Product, Student, Demotable


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


# admin.site.register(Product, ProductAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','mark','colllege')


admin.site.register(Student,StudentAdmin)



class DemoAdmin(admin.ModelAdmin):

    list_display = ('name','price','description')

admin.site.register(Demotable,DemoAdmin)