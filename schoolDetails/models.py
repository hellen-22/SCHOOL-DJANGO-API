from random import choices
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import validators

from account.models import *


class School(models.Model):
    school_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school')
    department_name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Unit(models.Model):
    unit_name = models.CharField(max_length=255)
    unit_code = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.unit_name

class UnitDetails(models.Model):
    REGISTRATION_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No')
    )
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='units')
    student_id = models.ForeignKey('account.Student', on_delete=models.CASCADE, related_name='units')
    registration_status = models.CharField(max_length=255, choices=REGISTRATION_CHOICES)

    def __str__(self) -> str:
        return self.unit.unit_name 

    
class Hostel(models.Model):
    hostel_name = models.CharField(max_length=200)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self) -> str:
        return self.hostel_name

    class Meta:
        ordering = ['capacity']


class StudentHostel(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    student = models.ForeignKey('account.Student', on_delete=models.CASCADE, related_name='student_hostel')
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='hostel')
    payment_status = models.CharField(max_length=200, choices=PAYMENT_STATUS_CHOICES)

    def __str__(self) -> str:
        return f'{self.student.first_name} {self.student.last_name}'


class Exam(models.Model):
    EXAM_TYPE_CHOICES = (
        ('SUP', 'SUPPLEMENTARY EXAM'),
        ('SPE', 'SPECIAL EXAM'),
        ('RE', 'RETAKE EXAM')
        ('MAIN', 'MAIN EXAM')
    )
    exam_type = models.CharField(max_length=200, choices=EXAM_TYPE_CHOICES)
    date = models.DateTimeField()

    def __str__(self) -> str:
        return self.exam_type

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey('account.Student', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    cat = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    exam = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(70)])

    def __str__(self) -> str:
        return self.exam.exam_type

class Attendance(models.Model):
    date = models.DateTimeField(auto_now=True)
    student = models.ForeignKey('account.Student', on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.date

    