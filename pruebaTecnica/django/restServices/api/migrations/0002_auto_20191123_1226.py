# Generated by Django 2.2.7 on 2019-11-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responsable',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
