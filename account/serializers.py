from pyexpat import model
from attr import field
from django.db import transaction
from django.db.models import Q
from rest_framework import serializers

from .models import *
from schoolDetails.models import *
from schoolDetails.serializers import UnitSerializer
from custom.models import User
from custom.serializers import UserCreateSerializer

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name']


class StudentSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            username = user['username']
            email = user['email']
            first_name = user['first_name']
            last_name = user['last_name']
            password = user['password']

            student_reg_no = self.validated_data['reg_no']
            student_department = self.validated_data['department']

            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            
            return Student.objects.create(reg_no=student_reg_no, department=student_department, user=user)

    class Meta:
        model = Student
        fields = ['id', 'reg_no', 'department', 'user', 'units']



class LecturerSerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()

    def save(self, **kwargs):
        with transaction.atomic():
            user = dict(self.validated_data['user'])
            username = user['username']
            email = user['email']
            first_name = user['first_name']
            last_name = user['last_name']
            password = user['password']

            lecturer_staff_id = self.validated_data['staff_id']
            lecturer_department = self.validated_data['department']

            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            
            return Lecturer.objects.create(staff_id=lecturer_staff_id, department=lecturer_department, user=user)

    class Meta:
        model = Lecturer
        fields = ['id', 'staff_id', 'department', 'user']



class UnitDetailSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    class Meta:
        model = UnitDetails
        fields = ['unit', 'registration_status']


class CreateUnitDetailSerializer(serializers.ModelSerializer):
        
    def save(self, **kwargs):
        unit = self.validated_data['unit']
        student_id = self.context['student_id']

        """
        Bug- the student is saving a unit twice
        if UnitDetails.objects.filter(Q(unit_id__gt=0) & Q(student_id__gt=0)):
            raise serializers.ValidationError("The Student already has the Unit")
        else:
            return UnitDetails.objects.create(unit=unit, student_id=student_id)

        """
        return UnitDetails.objects.create(unit=unit, student_id=student_id)

    class Meta:
        model = UnitDetails
        fields = ['unit']

class UpdateUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitDetails()
        fields = ['registration_status']


class HostelDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = ['hostel_name']

class StudentHostelDetailsSerializer(serializers.ModelSerializer):
    hostel = HostelDetailsSerializer()
    class Meta:
        model = StudentHostel
        fields = ['id', 'hostel', 'payment_status']

class CreateStudentHostelSerializer(serializers.ModelSerializer):
    payment_status = serializers.CharField(max_length=200, read_only=True)
    def save(self, **kwargs):
        hostel = self.validated_data['hostel']
        student_id = self.context['student_id']

        return StudentHostel.objects.create(hostel=hostel, student_id=student_id)
    class Meta:
        model = StudentHostel
        fields = ['id', 'hostel', 'payment_status']

class UpdateStudentHostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHostel
        fields = ['payment_status']


class StudentResultsSerializer(serializers.ModelSerializer):
    unit = UnitSerializer()
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Result
        fields = ['id', 'unit', 'cat', 'exam', 'total']

