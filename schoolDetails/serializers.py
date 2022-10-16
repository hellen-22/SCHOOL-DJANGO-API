from rest_framework import serializers

from .models import *
from account.models import Student

class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['reg_no', 'first_name', 'last_name']

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
        fields = ['id', 'hostel_name', 'capacity', 'student']
    

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_type', 'date' ]


class ViewUnitResultSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    student = StudentDetailsSerializer()

    class Meta:
        model = Result
        fields = ['id', 'unit', 'student']



class UnitResultSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        unit_id = self.context['unit_id']

        return Result.objects.create(unit_id=unit_id, **validated_data)

    class Meta:
        model = Result
        fields = ['id', 'student','unit', 'cat', 'exam']