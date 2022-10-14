from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'department_name']


class SchoolSerializer(serializers.ModelSerializer):
    number_of_departments = serializers.IntegerField(read_only=True)
    departments = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = School
        fields = ['id', 'school_name', 'departments', 'number_of_departments']


class CreateDepartmentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        school_id = self.context['school_id']
        department_name = self.validated_data['department_name']
        
        department = Department.objects.create(school_id=school_id, department_name=department_name)
        self.instance = department
        return self.instance


    class Meta:
        model = Department
        fields = ['id', 'department_name']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'unit_name', 'unit_code']


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['id', 'hostel_name', 'capacity']
