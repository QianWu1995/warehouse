from django.shortcuts import render
from django.contrib.auth.models import User
from users.form import RegistrationForm,log_in_form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import auth_login
# Create your views here.
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'register.html')


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})


def log_in(request):

    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return render(request,'home.html')
        else:
            return render(request, 'login.html')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def profile(request):
    user = request.user
    return render(request, 'profile.html',{'user':user})