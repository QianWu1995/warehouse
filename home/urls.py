
from django.contrib import admin
from django.urls import path, re_path
from home.views import home


urlpatterns = [


    path('', home),

]