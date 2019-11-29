# Generated by Django 2.2.7 on 2019-11-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20191127_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='estado',
            field=models.CharField(choices=[('Buen Estado', 'Buen Estado'), ('Mal estado', 'Mal estado'), ('Nuevo', 'Nuevo')], max_length=40),
        ),
        migrations.AlterField(
            model_name='responsable',
            name='telefono',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]