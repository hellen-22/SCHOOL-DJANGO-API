from django.contrib import admin
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.db.models.aggregates import Count

from schoolDetails.models import *

# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ['school_name', 'number_of_departments']

    @admin.display(ordering='total_departments')
    def number_of_departments(self, school:School):
        url = (
            reverse('admin:schoolDetails_department_changelist')
            + '?'
            + urlencode({
                'school__id': str(school.id)
            }))
        return format_html('<a href="{}">{} </a>', url, school.total_departments)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(total_departments=Count('school'))

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
    list_display = ['unit_code', 'registration_status']
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