from django.urls import path
from hotel import urls
from employeeRec import urls
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('video_stream/', views.video_stream, name='video_stream'),
    path('add_photos/', views.add_photos, name='add_photos'),
    path('add_photos/<slug:emp_id>/', views.click_photos, name='click_photos'),
    path('train_model/', views.train_model, name='train_model'),
    path('detected/', views.detected, name='detected'),
    path('identify/', views.identify, name='identify'),
    path('add_emp/', views.add_emp, name='add_emp'),
    
]
