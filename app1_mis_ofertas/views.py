from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import InfoUsuarioForm, ProductoForm
from django.contrib.auth.decorators import login_required
from .models import InfoUsuario, Producto

#Colores hexadecimales para el proyecto
#590012
#6c0d21
#801a2f
#93273e
#a6344c

def home(request):
    user = request.user
    return render(request, 'index.html', {
        'usuario': user.is_superuser
    })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('home')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'campo': InfoUsuarioForm,
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                infoUsuario = InfoUsuario.objects.create(user=user, rut=request.POST['rut'], nombre=request.POST['nombre'], apellido=request.POST['apellido'])
                infoUsuario.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Las Contraseñas no coinciden'
                })
    
def signout(request):
    logout(request)
    return redirect('home')

def post_product(request):
    return render(request, 'post.html', {
        'form': ProductoForm
    })