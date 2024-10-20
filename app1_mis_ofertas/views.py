from django.shortcuts import render

#Colores hexadecimales para el proyecto
#590012
#6c0d21
#801a2f
#93273e
#a6344c

def home(request):
    return render(request, 'index.html')