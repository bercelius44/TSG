# Generated by Django 2.2.7 on 2019-11-28 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_remove_resources_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='id_encargado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.Responsable', verbose_name='Responsables'),
        ),
    ]
