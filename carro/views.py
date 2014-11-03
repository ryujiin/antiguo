from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse, Http404
from serializers import CarroSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from models import *

class CarritoViewsApi(APIView):
	def get(self,request,format=None):
		carro = Carro.objects.all()
		serializer = CarroSerializer(carro,many=True)
		return Response(serializer.data,status=status.HTTP_200_OK)
		"""
		if 'carrito' in request.COOKIES :
			coockie_carro = request.COOKIES["carrito"]	
			if request.user.is_authenticated():
				carro = Carro.objects.filter(propietario= request.user,estado='Abierto').order_by('-date_submitted')[:1]
				if not carro:
					carro = Carro.objects.filter(sesion_carro=coockie_carro,estado='Abierto').order_by('-date_submitted')[:1]
					if carro:
						for car in carro:
							car.propietario=request.user
							car.save()
			else:
				carro = Carro.objects.filter(sesion_carro=coockie_carro,estado='Abierto').order_by('-date_submitted')[:1]
			serializer = CarroSerializer(carro,many=True)
			return Response(serializer.data)
		else:
			carro = Carro.objects.filter(estado='Nunca lo encontraras').order_by('-date_submitted')[:1]
			serializer = CarroSerializer(carro,many=True)
			return Response(serializer.data,status=status.HTTP_200_OK)
		"""

	def post(self, request, format=None):
		serializer = CarroSerializer(data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	

class CarritoDetailViews(APIView):
	def get_object(self,pk):
		try:
			return Carro.objects.get(pk=pk)
		except Carro.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		carro = self.get_object(pk)
		serializer = CarroSerializer(carro)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		carro = self.get_object(pk)
		serializer = CarroSerializer(carro,data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data)
		return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)