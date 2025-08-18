from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('id', 'name')

#,'contact_number','date_of_birth','date_of_joining','department','designation','gender','team'
