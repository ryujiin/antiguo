from django.shortcuts import render
from models import Categoria,Producto
from serializers import ProductoListaSerializer,ProductoSingleSereializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
from rest_framework import viewsets

class CategoriaViewsets(viewsets.ReadOnlyModelViewSet):
	model = Categoria

class ProductoListaViewsets(viewsets.ModelViewSet):
	model = Producto
	serializer_class = ProductoListaSerializer

class CatalogoViewsets(viewsets.ReadOnlyModelViewSet):
	model = Producto
	serializer_class = ProductoSingleSereializer