from django.contrib import admin

from account.models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = ['reg_no', 'first_name', 'last_name']
    ordering = ['user__first_name', 'user__last_name']
    autocomplete_fields = ['user']

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ['staff_id', 'first_name', 'last_name']
    ordering = ['user__first_name', 'user__last_name']
    autocomplete_fields = ['user']

