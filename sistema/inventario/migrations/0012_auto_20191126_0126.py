# Generated by Django 2.1.3 on 2019-11-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0011_remove_opciones_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='correo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='correo2',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
