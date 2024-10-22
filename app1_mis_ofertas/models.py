from django.db import models
from django.contrib.auth.models import User


class InfoUsuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    correo = models.EmailField(max_length=50)

    def __str__(self):
        return f'{self.user.first_name}'
    