from django.shortcuts import render
from django.db.models import F
from rest_framework.mixins import  RetrieveModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAdminUser

from .serializers import *
from .models import *
from schoolDetails.permissions import IsAdminOrReadOnly

# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAdminUser]

class LecturerViewSet(ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = [IsAdminUser]


class UnitDetailsViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        return UnitDetails.objects.filter(student_id=self.kwargs['student_pk'])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUnitDetailSerializer
        elif self.request.method == 'PATCH':
            return UpdateUnitSerializer
        return UnitDetailSerializer

    def get_serializer_context(self):
        return {'student_id': self.kwargs['student_pk']}

class StudentHostelViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    
    def get_queryset(self):
        return StudentHostel.objects.filter(student_id=self.kwargs['student_pk'])

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateStudentHostelSerializer
        elif self.request.method == 'PATCH':
            return UpdateStudentHostelSerializer
        return StudentHostelDetailsSerializer

    def get_serializer_context(self):
        return {'student_id': self.kwargs['student_pk']}

class StudentResultViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = StudentResultsSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get_queryset(self):
        return Result.objects.select_related('unit').annotate(total=F('cat') + F('exam')).filter(student_id=self.kwargs['student_pk'])