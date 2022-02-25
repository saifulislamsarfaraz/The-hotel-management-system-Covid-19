from unicodedata import name
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



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

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="hotels/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="hotels/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="hotels/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="hotels/password_reset_done.html"), 
        name="password_reset_complete"),
]
