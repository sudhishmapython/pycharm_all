from django.contrib import admin

from demoapp.models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display =('name', 'price', 'description')

admin.site.register(Product,ProductAdmin)