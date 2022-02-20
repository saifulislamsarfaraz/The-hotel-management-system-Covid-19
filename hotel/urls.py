from unicodedata import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:id>',views.show,name='show'),
    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('login/Register.html', views.registerPage,name='register'),
    path('register/Login.html', views.registerPage,name='register'),
    path('hotels/Register.html',views.registerPage,name='register'),
    path('deshboard/',views.deshBoard,name='deshboard'),
]
