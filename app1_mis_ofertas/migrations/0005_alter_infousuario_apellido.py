# Generated by Django 4.1.2 on 2024-10-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1_mis_ofertas', '0004_infousuario_apellido_infousuario_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infousuario',
            name='apellido',
            field=models.CharField(default='Sin apellido', max_length=50),
        ),
    ]