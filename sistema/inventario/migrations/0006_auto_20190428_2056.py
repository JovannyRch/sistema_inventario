# Generated by Django 2.1.3 on 2019-04-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_auto_20190418_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.CharField(max_length=100),
        ),
    ]
