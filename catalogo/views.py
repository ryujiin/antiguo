from django.shortcuts import render
from models import *
from serializers import ProductoListaSerializer,ProductoSingleSereializer,CategoriaSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
from rest_framework import viewsets

class CategoriaViewsets(viewsets.ReadOnlyModelViewSet):
	model = Categoria
	serializer_class = CategoriaSerializer	

class ProductoListaViewsets(viewsets.ModelViewSet):
	model = Producto
	serializer_class = ProductoListaSerializer

class Producto_singleViewstes(viewsets.ModelViewSet):
	model = Producto
	serializer_class = ProductoSingleSereializer
		

class CatalogoViewsets(viewsets.ReadOnlyModelViewSet):
	serializer_class = ProductoListaSerializer

	def get_queryset(self):
		queryset = Producto.objects.all()
		return queryset

##Catalogo##

class ColorViewsets(viewsets.ReadOnlyModelViewSet):
	model = Color

class GeneroViewsets(viewsets.ReadOnlyModelViewSet):
	model = Genero

class TallaViewsets(viewsets.ReadOnlyModelViewSet):
	model = Talla

class SeccionViewsets(viewsets.ReadOnlyModelViewSet):
	model = Seccion

class EstiloViewsets(viewsets.ReadOnlyModelViewSet):
	model = Estilo
