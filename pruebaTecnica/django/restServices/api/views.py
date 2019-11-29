from rest_framework import generics, request
from .serializers import ResponsableSerializer, ResourcesSerializer
from .models import Responsable, Resources
from rest_framework.response import Response


class ResponsableGetViewSet(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ResponsableSerializer    

    def get_queryset(self):
        return Responsable.objects.all()

    def get(self, request, *args, **kwargs):
        user = self.kwargs['nombre']
        responsables = Responsable.objects.filter(nombre=user)
        serializer = ResponsableSerializer(responsables, many = True)
        return Response(serializer.data)

class ResponsablesGetViewSet(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ResponsableSerializer

    def get_queryset(self):
        return Responsable.objects.all()

class ResponsablePostViewSet(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = ResponsableSerializer

    def get_queryset(self):
        return Responsable.objects.all()

class ResponsablePutPatchViewSet(generics.UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ResponsableSerializer

    def get_queryset(self):
        return Responsable.objects.all()

class ResponsableDeleteViewSet(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ResponsableSerializer

    def get_queryset(self):
        return Responsable.objects.all()

class ResourcesGetViewSet(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ResourcesSerializer

    def get_queryset(self):
        return Resources.objects.all()

class ResourceGetSerieViewSet(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ResourcesSerializer

    def get_queryset(self):
        return Resources.objects.all()
    
    def get(self, request, *args, **kwargs):
        user = self.kwargs['pk']
        resource = Resources.objects.filter(serial=user)
        serializer = ResourcesSerializer(resource, many = True)
        return Response(serializer.data)

class ResourceGetTipoViewSet(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ResourcesSerializer

    def get_queryset(self):
        return Resources.objects.all()
    
    def get(self, request, *args, **kwargs):
        user = self.kwargs['tipo']
        resource = Resources.objects.filter(tipo = user)
        serializer = ResourcesSerializer(resource, many = True)
        return Response(serializer.data)

class ResourceGetMarcaViewSet(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ResourcesSerializer

    def get_queryset(self):
        return Resources.objects.all()
    
    def get(self, request, *args, **kwargs):
        user = self.kwargs['marca']
        resource = Resources.objects.filter(marca = user)
        serializer = ResourcesSerializer(resource, many = True)
        return Response(serializer.data)

class ResourcesPostViewSet(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = ResourcesSerializer

    def get_queryset(self):
        return Resources.objects.all()

class ResourcesPutPatchViewSet(generics.UpdateAPIView):
    lookup_field = 'pk'
    serializer_class = ResourcesSerializer

    def get_queryset(self):
        return Resources.objects.all()

class ResourcesDeleteViewSet(generics.DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ResourcesSerializer

    def get_queryset(self):
        return Resources.objects.all()



    # queryset = Responsable.objects.all()
    # serializer_class = ResponsableSerializer 

    # def list(self, request, *args, **kwargs):
    #     responsables = Responsable.objects.all()        
    #     serializer = ResponsableMiniSerializer(responsables, many = True)
    #     return Response(serializer.data)

# class ResourcesViewSet(viewsets.ModelViewSet):
#     queryset = Resources.objects.all()
#     serializer_class = ResourcesSerializer

#     def list(self, request, *args, **kwargs):
#         resources = Resources.objects.all()
#         serializer = ResourcesMiniSerializer(resources, many = True)
#         return Response(serializer.data)

# class ResponsableViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    
#     queryset = Responsable.objects.all()
#     serializer_class = ResponsableSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, *kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)