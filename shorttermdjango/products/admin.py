from django.contrib import admin
from .models import  Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','image')


# Register your models here.
# admin.site.register(Product)
admin.site.register(Product,ProductAdmin)




