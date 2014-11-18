from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from rest_framework import routers
from catalogo.views import CategoriaViewsets,ProductoListaViewsets,CatalogoViewsets
from cliente.views import UsuarioViewSet,ObtainAuthToken
from carro.views import LineasViewsets
from ubigeo.views import RegionViewset

router = routers.DefaultRouter()

router.register(r'listaproducto', ProductoListaViewsets)
router.register(r'categoria', CategoriaViewsets)
router.register(r'catalogo', CatalogoViewsets,'productosingle')
router.register(r'usuario',UsuarioViewSet)
router.register(r'lineas',LineasViewsets,'lineas')
router.register(r'ubigeo',RegionViewset,'ubigeo')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/cliente/', include('cliente.urls')),
    url(r'^api/carro/', include('carro.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    url(r'^api-token/login/(?P<backend>[^/]+)/$',ObtainAuthToken.as_view()),
    url(r'^register/(?P<backend>[^/]+)/', 'cliente.views.register_by_access_token'),
    url('', include('social.apps.django_app.urls',namespace="social")),


    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + urlpatterns