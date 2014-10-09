from django.shortcuts import render
from models import Categoria,Producto
from serializers import ProductoListaSerializer

# Create your views here.
from rest_framework import viewsets

class CategoriaViewsets(viewsets.ModelViewSet):
	model = Categoria

class ProductoListaViewsets(viewsets.ModelViewSet):
	model = Producto
	serializer_class = ProductoListaSerializer