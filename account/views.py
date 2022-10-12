from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class LecturerViewSet(ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer