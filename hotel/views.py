from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

from hotel.decorators import unauthenticated_user
from .models import Room

from .forms import ContactForm,BookingRoomForm
from .forms import VacinationsStatusForm
from hotel.bookingFunctions.availability import check_availability

from .decorators import unauthenticated_user, allowed_users, admin_only
# Create your views here.
from .models import * 

CACHE_TTL = getattr(settings,'CACHE_TTL',DEFAULT_TIMEOUT)

from .forms import CreateUserForm

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('deshboard')
        
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)

                return redirect('login')


        context = {'form':form}
        return render(request,'hotel/Register.html',context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('deshboard')
        else:
            messages.info(request,'Username OR Password is incorrect')

    context = {}
    return render(request,'hotel/Login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def deshBoard(request):
    context = {}
    return render(request,'hotel/deshboard.html',context)





def get_room(filter_room=None):
    if filter_room:
        print("DATA COMING FROM DB")
        room = Room.objects.filter(category__contains = filter_room)
    else:
        room = Room.objects.all()
    return room


def home(request):
    filter_room = request.GET.get('room')
    if cache.get(filter_room):
        print("DATA COMING FROM CACHE")
        room = cache.get(filter_room)
    else:
        if filter_room:
            room = get_room(filter_room)
            cache.set(filter_room,room)
        else:
            room = get_room()
    context = {'room':room}
    return render(request,'hotel/home.html',context)

#@login_required(login_url='login')
def show(request,id):
    if cache.get(id):
      
        room = cache.get(id)
    else:
        room = Room.objects.get(id=id)
        cache.set(id,room)
    context = {'room':room}
    return render(request,'hotel/show.html',context)

@login_required(login_url='login')
def employee(request):
    return render(request,'employeeRec/index.html')


def hotelsection(request):
    return render(request,'hotel/home.html')



def contactus(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return render(request,'hotel/home.html')
    else:
        form = ContactForm()
    return render(request, 'hotel/contact.html', {'form': form})


def bookingForm(request):

    form = BookingRoomForm()
    if(request.method=='POST'):
        form = BookingRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'hotel/home.html')
    context = {'form':form}
    return render(request,'hotel/booking_form.html',context)





