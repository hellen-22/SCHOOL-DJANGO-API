from django.contrib import admin

from schoolDetails.models import *

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'department_name']
    autocomplete_fields = ['school']

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass

@admin.register(UnitDetails)
class UnitDetailsAdmin(admin.ModelAdmin):
    list_display = ['unit_name', 'registration_status']
    autocomplete_fields = ['unit']

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display = ['hostel_name', 'capacity']

@admin.register(StudentHostel)
class StudentHostelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'payment_status']
    autocomplete_fields = ['student', 'hostel', 'payment_status']

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['date', 'unit_name', 'reg_no']

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    pass