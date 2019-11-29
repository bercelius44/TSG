from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Responsable, Resources

class ResponsableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsable
        fields = ['id','nombre', 'telefono', 'tipo']

class ResourcesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resources
        fields = ['serial', 'id_encargado', 'marca', 'tipo', 'proveedor', 'valor_comercial', 'fecha_compra', 'estado', 'fecha_asignacion']