from venv import create
from django.shortcuts import render
from django.db.models.aggregates import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import *
from .serializers import *
from .permissions import *

# Create your views here.
class SchoolViewSet(ModelViewSet):
    queryset = School.objects.annotate(number_of_departments=Count('departments')).prefetch_related('departments__school').all()
    serializer_class = SchoolSerializer
    permission_classes = [IsAdminOrReadOnly]


class DepartmentViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    permission_classes = [IsAdminOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateDepartmentSerializer
        return DepartmentSerializer

    def get_serializer_context(self):
        return {'school_id': self.kwargs['school_pk']}

    def get_queryset(self):
        return Department.objects.select_related('school').filter(school_id=self.kwargs['school_pk'])


class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer