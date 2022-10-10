from random import choices
from turtle import mode
from django.db import models

from account.models import *


class School(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school')
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Unit(models.Model):
    unit_name = models.CharField(max_length=255)
    unit_code = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.unit_name

class UnitDetails(models.Model):
    REGISTRATION = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='units')
    student_id = models.ForeignKey('account.Student', on_delete=models.CASCADE)
    registration_status = models.CharField(max_length=255, choices=REGISTRATION)