from django.contrib import admin

from schoolDetails.models import *

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ['']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ['school_name', 'department_name']
    autocomplete_fields = ['school']

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    search_fields = ['']

@admin.register(UnitDetails)
class UnitDetailsAdmin(admin.ModelAdmin):
    list_display = ['unit_code', 'reg_no', 'registration_status']
    autocomplete_fields = ['unit', 'student']

@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ['hostel_name', 'capacity']

@admin.register(StudentHostel)
class StudentHostelAdmin(admin.ModelAdmin):
    list_display = ['reg_no', 'first_name', 'last_name', 'payment_status']
    autocomplete_fields = ['student', 'hostel']

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ['reg_no', 'unit_code', 'cat', 'exam', 'total']
    autocomplete_fields = ['student', 'unit']

    @admin.display(ordering='total')
    def total(self, result:Result):
        return result.cat + result.exam

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    autocomplete_fields = ['student', 'unit']
    list_display = ['date', 'reg_no', 'unit_code']