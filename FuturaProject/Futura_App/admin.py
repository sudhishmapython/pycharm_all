from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from Futura_App import models

admin.site.register(models.Person)
admin.site.register(models.Student)
admin.site.register(models.Attendance)



class PersonAdmin(ImportExportModelAdmin):
    list_display = ('intern', 'staff', 'mark')