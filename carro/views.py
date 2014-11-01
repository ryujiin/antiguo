from django.shortcuts import render
from rest_framework import viewsets

from models import *

class PruebaViewset(viewsets.ModelViewSet):
	model = Prueba

class CarroViewSet(viewsets.ModelViewSet):
	model = Carro

	def pre_save(self,obj):
		if self.request.user.is_authenticated():
			obj.propietario = self.request.user

	def get_queryset(self):
		if self.request.user.is_authenticated():
			carrito = Carro.objects.filter(propietario=self.request.user,estado='Abierto').order_by('-date_submitted')[:1]
		else:
			carrito = Carro.objects.filter(estado='Nunca lo encontraras').order_by('-date_submitted')[:1]
		return carrito