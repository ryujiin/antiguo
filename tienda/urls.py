from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
	url(r'^$',HomeView.as_view() , name='home'),
	url(r'^catalogo/$',HomeView.as_view() , name='catalogo'),
	url(r'^producto/',HomeView.as_view() , name='producto'),
	url(r'^perfil/',HomeView.as_view() , name='perfil'),
)
