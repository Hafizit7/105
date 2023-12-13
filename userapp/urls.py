from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

path('register/', register, name='register'),

path('login/', auth_views.LoginView.as_view(template_name='userapp/login.html'), name='login'),
path('logout/', auth_views.LogoutView.as_view(template_name='store/index.html'), name='logout'),

path('dashboard/', dashboard, name='dashboard')
    
]