# Generated by Django 4.1.2 on 2024-10-22 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1_mis_ofertas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infousuario',
            name='Correo',
        ),
        migrations.RemoveField(
            model_name='infousuario',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='infousuario',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='infousuario',
            name='password',
        ),
    ]