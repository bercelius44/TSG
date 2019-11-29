from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from api import views
from api.models import Responsable, Resources
from api.serializers import ResponsableSerializer, ResourcesSerializer

#router = routers.DefaultRouter()
#router.register(r'responsable', views.ResponsableViewSet.as_view(), basename='Responsable')
#router.register(r'resources', views.ResourcesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-responsables/$', views.ResponsablesGetViewSet.as_view(queryset=Responsable.objects.all(), serializer_class=ResponsableSerializer), name='responsables-list'),
    url(r'^get-responsable=(?P<nombre>[\w ]+)/$', views.ResponsableGetViewSet.as_view(queryset=Responsable.objects.all(), serializer_class=ResponsableSerializer), name='responsable-list'),
    url(r'^create-responsable/$', views.ResponsablePostViewSet.as_view(queryset=Responsable.objects.all(), serializer_class=ResponsableSerializer), name='responsable-create'),
    url(r'^update-responsable=(?P<pk>\d+)/$', views.ResponsablePutPatchViewSet.as_view(queryset=Responsable.objects.all(), serializer_class=ResponsableSerializer), name='responsable-update'),
    url(r'^delete-responsable=(?P<pk>\d+)/$', views.ResponsableDeleteViewSet.as_view(queryset=Responsable.objects.all(), serializer_class=ResponsableSerializer), name='responsable-delete'),
    url(r'^get-resources/$', views.ResourcesGetViewSet.as_view(queryset=Resources.objects.all(), serializer_class=ResourcesSerializer), name='resources-list'),
    url(r'^get-resource-serial=(?P<pk>\d+)/$', views.ResourceGetSerieViewSet.as_view(queryset=Resources.objects.all(), serializer_class=ResourcesSerializer), name='resource-list-by-serial'),
    url(r'^get-resource-tipo=(?P<tipo>[\w ]+)/$', views.ResourceGetTipoViewSet.as_view(queryset=Resources.objects.all(), serializer_class=ResourcesSerializer), name='resources-list-by-type'),
    url(r'^get-resource-marca=(?P<marca>[\w ]+)/$', views.ResourceGetMarcaViewSet.as_view(queryset=Resources.objects.all(), serializer_class=ResourcesSerializer), name='resources-list-by-brand'),
    url(r'^create-resource/$', views.ResourcesPostViewSet.as_view(queryset=Resources.objects.all(), serializer_class=ResourcesSerializer), name='resource-create'),
    url(r'^update-resource=(?P<pk>\d+)/$', views.ResourcesPutPatchViewSet.as_view(queryset=Resources.objects.all(), serializer_class=ResourcesSerializer), name='resource-update'),
    url(r'^delete-resource=(?P<pk>\d+)/$', views.ResourcesDeleteViewSet.as_view(queryset=Resources.objects.all(), serializer_class=ResourcesSerializer), name='resource-delete'),
]