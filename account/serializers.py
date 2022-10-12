import email
from rest_framework import serializers

from .models import *
from schoolDetails.serializers import UnitSerializer
from custom.models import User

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class StudentSerializer(serializers.ModelSerializer):
    user = UserDetailsSerializer()
    def create(self, validated_data):
        user = self.validated_data['user']
        
        if not Lecturer.objects.filter(user=user).count() == 0:
            raise serializers.ValidationError("User is already a lecturer")
        
        return Student.objects.create(**validated_data)

    class Meta:
        model = Student
        fields = ['id', 'reg_no', 'department', 'user']

class LecturerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = validated_data['user']
        if not Student.objects.filter(user=user).count() == 0:
            raise serializers.ValidationError("User is already a lecturer")
        
        return Lecturer.objects.create(**validated_data)

    class Meta:
        model = Lecturer
        fields = ['id', 'staff_id', 'department', 'user']

    

