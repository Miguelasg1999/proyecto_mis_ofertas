from django import forms
from .models import InfoUsuario

class InfoUsuarioForm(forms.ModelForm):
    class Meta:
        model = InfoUsuario
        fields = ['rut', 'nombre', 'apellido']