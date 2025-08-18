from django.urls import path


from .import views



urlpatterns = [  
    path('takeappointment/',views.takeappoinment,name='takeappointment'),
    path('appointment/',views.apoinment,name='appointment'),
    path('healthhome/',views.healthHome,name='healthhome'),
]
