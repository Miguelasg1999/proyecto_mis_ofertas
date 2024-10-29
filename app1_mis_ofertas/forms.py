from django import forms
from .models import InfoUsuario, Producto

class InfoUsuarioForm(forms.ModelForm):
    class Meta:
        model = InfoUsuario
        fields = ['rut', 'nombre', 'apellido']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']