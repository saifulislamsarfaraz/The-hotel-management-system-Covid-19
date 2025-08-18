from django.shortcuts import render
from .models import Appointment
from hotel import urls
from employeeRec import urls
from .forms import BookForm,AppointmentForm

def apoinment(request):

    form = AppointmentForm()
    if(request.method=='POST'):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'healthcare/healthHome.html')
    context = {'form':form}
    return render(request,'healthcare/appointment.html',context)


def takeappoinment(request):

    form = BookForm()
    if(request.method=='POST'):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'healthcare/healthHome.html')
    context = {'form':form}
    return render(request,'healthcare/appointment_form.html',context)

def healthHome(request):
    return render(request,'healthcare/healthHome.html')
    