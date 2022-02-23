
from atexit import register
from dataclasses import fields
from tkinter.tix import Form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 
class CreateRegisterForm(forms.models):
    class Meta:
        model = Register
        fields = ['Id','name']

