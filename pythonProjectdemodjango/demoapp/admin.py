from django.contrib import admin


from demoapp.models import Student, SutudRadio


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mark', 'place')

admin.site.register(Student,StudentAdmin)


admin.site.register(SutudRadio)
