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

class CatalogoViewsets(viewsets.ReadOnlyModelViewSet):
	model = Producto
	serializer_class = ProductoSingleSereializer


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
