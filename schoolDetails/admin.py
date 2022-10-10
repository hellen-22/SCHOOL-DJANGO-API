from django.contrib import admin

from schoolDetails.models import *

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass