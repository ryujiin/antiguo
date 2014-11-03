from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings

from rest_framework import routers
from catalogo.views import CategoriaViewsets,ProductoListaViewsets,ProductoSingleViewsets
from cliente.views import UsuarioViewSet

router = routers.DefaultRouter()

router.register(r'listaproducto', ProductoListaViewsets)
router.register(r'categoria', CategoriaViewsets)
router.register(r'productosingle', ProductoSingleViewsets,'productosingle')
router.register(r'usuario',UsuarioViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/cliente/', include('cliente.urls')),
    url(r'^api/carro/', include('carro.urls')),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),

    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
) + urlpatterns