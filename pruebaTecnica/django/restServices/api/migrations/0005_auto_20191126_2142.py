# Generated by Django 2.2.7 on 2019-11-27 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20191126_2135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='responsable',
            options={'verbose_name_plural': 'Responsables'},
        ),
        migrations.AlterField(
            model_name='resources',
            name='id_encargado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='api.Responsable', verbose_name='Responsables'),
        ),
    ]
