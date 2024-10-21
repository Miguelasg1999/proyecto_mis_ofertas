from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
#from .forms import 

#Colores hexadecimales para el proyecto
#590012
#6c0d21
#801a2f
#93273e
#a6344c

def home(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')