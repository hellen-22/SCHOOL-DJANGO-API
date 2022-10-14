from django.db import transaction
from rest_framework import serializers

from .models import *
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
        fields = ['id', 'reg_no', 'department', 'user']



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

    

