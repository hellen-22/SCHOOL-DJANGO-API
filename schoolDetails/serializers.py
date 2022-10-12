from pyexpat import model
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

    """
    #Unsolved Adding a department to a School that does not exists
    def validate_school_id(self, *kwargs, value):
        if not School.objects.filter(pk=self.kwargs['school_pk']):
            raise serializers.ValidationError('The school does not exists. Create school first')
        return value
    """
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