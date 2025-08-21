<<<<<<< HEAD

from atexit import register
from dataclasses import fields
from tkinter.tix import Form
=======
>>>>>>> origin/improvements
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

<<<<<<< HEAD
=======
from django.core.exceptions import ValidationError
from .models import Room



>>>>>>> origin/improvements

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 


<<<<<<< HEAD
=======
from datetime import datetime
from django.core.exceptions import ValidationError
from .models import RoomCategory,BookingRoom

#  input_formats=["%Y-%m-%dT%H:%M", ],



from .models import VacinationStatus
from .models import ContactUs

class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ('name','email','phone','message')

class BookingRoomForm(forms.ModelForm):
    class Meta:
        model = BookingRoom
        fields = '__all__'
        

class VacinationsStatusForm(forms.ModelForm):
    class Meta:
        model = VacinationStatus
        fields = ('username','vacinationCirtificateNum','totalDose','covidTest')
>>>>>>> origin/improvements
