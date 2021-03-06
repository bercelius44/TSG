# Generated by Django 2.2.7 on 2019-11-23 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191123_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=False, serialize=False, verbose_name='ID')),
                ('id_encargado', models.IntegerField()),
                ('marca', models.CharField(max_length=40)),
                ('tipo', models.CharField(max_length=40)),
                ('proveedor', models.CharField(max_length=40)),
                ('valor_comercial', models.CharField(max_length=40)),
                ('fecha_compra', models.DateField()),
                ('estado', models.CharField(max_length=40)),
                ('fecha_asignacion', models.DateField()),
            ],
        ),
    ]
