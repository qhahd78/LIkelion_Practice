from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserForm

# Create your views here.

def home(request) : 
    form = UserForm()
    return render(request, 'home.html')

def signup(request) : 
    form = UserCreationForm()
    if request.method == "POST" : 
        filld_form = UserCreationForm(request.POST)
        if filled_form.is_valid(): 
            filld_form.save()
            return redirect('home')
        else : 
            pass
    return render(request, 'signup.html', {'form':form})

def signin(request) : 


class MyLoginView(LoginView):
    template_name = 'signin.html'


class MyLogoutView(LogoutView):
    template_name 