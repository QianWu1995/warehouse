
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, re_path
from punch.views import punch_in
from warehouse.views import home_page_redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('', punch_in),

]