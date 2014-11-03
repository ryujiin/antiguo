from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    url(r'^',PerfilUserViewSet.as_view(),name='prefil_user'),
)