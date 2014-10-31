from django.shortcuts import render
from rest_framework import viewsets

from models import *

class PruebaViewset(viewsets.ModelViewSet):
	model = Prueba

class CarroViewSet(viewsets.ModelViewSet):
	model = Carro

	def pre_save(self,obj):
		obj.propietario = self.request.user