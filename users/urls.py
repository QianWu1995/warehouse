from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from users.views import register,log_in,profile
from warehouse.views import home_page_redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login/', log_in),
    path('profile/',profile),
    path('', register),
    #path('login/', auth_views.login, name='login')

]