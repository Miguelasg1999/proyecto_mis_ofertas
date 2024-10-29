from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import InfoUsuarioForm, ProductoForm
from django.contrib.auth.decorators import login_required
from .models import InfoUsuario, Producto


def home(request):
    user = request.user

    return render(request, 'index.html', {
        'usuario': user.is_superuser,
        'productos': Producto.objects.all()
    })

def main(request):
    return render(request, 'main.html')

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
@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def post_product(request):
    user = request.user
    if user.is_superuser:
        if request.method == 'GET':
            return render(request, 'post.html', {
            'form': ProductoForm
        })
        else:
            Producto.objects.create(nombre=request.POST['nombre'], descripcion=request.POST['descripcion'], precio=request.POST['precio'], imagen= request.FILES['imagen'])
            return redirect('home')
    else:
        return redirect('home')

 
def product(request, id):
    producto = Producto.objects.get(id=id)
    return render(request, 'product.html',{
        'producto': producto
    })

@login_required
def eliminarProd(request, id):
    user = request.user
    if user.is_superuser:
        producto = Producto.objects.get(id=id)
        producto.delete()
    return redirect(home)

@login_required
def editarProd(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editProd.html', {'form': form})