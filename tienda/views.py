from django.shortcuts import render
from django.views.generic import TemplateView
from models import *
class HomeView(TemplateView):
	template_name = "layout.html"


from rest_framework import viewsets

class Menu_principalViewsets(viewsets.ReadOnlyModelViewSet):
	model = Menu_principal