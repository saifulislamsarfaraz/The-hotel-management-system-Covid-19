from datetime import datetime
from sqlite3 import DateFromTicks
from time import time
from tkinter import Widget
from xmlrpc.client import DateTime
from django.contrib.auth.models import User
from django import forms
from .models import Appointment,TakeAppointment
from django.forms.widgets import DateInput
from django.contrib.admin.widgets import AdminDateWidget,AdminTimeWidget,AdminSplitDateTime

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = '__all__'
        Widgets = {
            "date" : AdminDateWidget(),
            "time" :AdminTimeWidget(),
        }

class BookForm(forms.ModelForm):

    class Meta:
        model = TakeAppointment
        fields = ['user','full_name','email','phone_number','date']
        Widgets = {
            "date" : AdminDateWidget(),
            "time" : AdminTimeWidget(),
        }