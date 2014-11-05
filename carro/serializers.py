from rest_framework import serializers
from models import *
from django.conf import settings
from catalogo.models import Producto

class CarroSerializer(serializers.ModelSerializer):
	lineas = serializers.SerializerMethodField('get_lineas')

	class Meta:
		model = Carro
		fields = ('id','propietario','estado','sesion_carro','lineas')

	def get_lineas(self,obj):
		return obj.num_lineas()

class LineaSerializer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField('get_thum')
	nombre = serializers.SerializerMethodField('get_nombre')
	talla = serializers.SerializerMethodField('get_talla')
	precio = serializers.SerializerMethodField('get_precio')
	subtotal = serializers.SerializerMethodField('get_subtotal')
	class Meta:
		model = LineaCarro
		fields = ('id','carro','producto','variacion','cantidad','thum','nombre','talla','precio','subtotal')

	def get_thum(self,obj):
		thum = obj.producto.get_thum
		return thum

	def get_nombre(self,obj):
		return obj.producto.full_name

	def get_talla(self,obj):
		return obj.variacion.talla

	def get_precio(self,obj):
		return obj.variacion.get_precio_venta

	def get_subtotal(self,obj):
		return obj.get_subtotal