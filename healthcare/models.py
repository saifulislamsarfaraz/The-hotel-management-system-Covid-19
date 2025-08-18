import email
from django.contrib.auth.models import User
from datetime import timezone
from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.

department = (
    ('High Temperature', "Covid Disease"),
    ('Heart Disease', "Heart Disease"),
    ('Diabetes Disease', "Diabetes Disease"),
    ('Breast Cancer', "Breast Cancer"),
    ('Dentistry', "Dentistry"),
    ('Cardiology', "Cardiology"),
    ('ENT Specialists', "ENT Specialists"),
    ('Astrology', 'Astrology'),
    ('Neuroanatomy', 'Neuroanatomy'),
    ('Blood Screening', 'Blood Screening'),
    ('Eye Care', 'Eye Care'),
    ('Physical Therapy', 'Physical Therapy'),
)


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    qualification_name = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=100)
    department = models.CharField(choices=department, max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.full_name

class TakeAppointment(models.Model):
    user = models.CharField(primary_key='user',max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=120)
    date = models.DateTimeField(null=True)

    def __str__(self):
        return self.full_name

