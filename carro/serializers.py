from rest_framework import serializers
from models import *
from django.conf import settings
from catalogo.models import Producto

class CarroSerializer(serializers.ModelSerializer):
	lineas = serializers.SerializerMethodField('get_lineas')
	total = serializers.SerializerMethodField('get_total')
	subtotal = serializers.SerializerMethodField('get_subtotal')
	envio = serializers.SerializerMethodField('get_envio')
	class Meta:
		model = Carro
		fields = ('id','propietario','estado','sesion_carro','lineas','total','subtotal','envio')

	def get_lineas(self,obj):
		lineas = obj.num_lineas()
		lineas = int(lineas)
		return lineas

	def get_total(self,obj):
		total =obj.total_carro()
		return '%0.2f' %(total)

	def get_subtotal(self,obj):
		subtotal = obj.subtotal_carro()
		return "%0.2f" %(subtotal)

	def get_envio(self,obj):
		return obj.envio_carro()

class LineaSerializer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField('get_thum')
	nombre = serializers.SerializerMethodField('get_nombre')
	talla = serializers.SerializerMethodField('get_talla')
	precio = serializers.SerializerMethodField('get_precio')
	subtotal = serializers.SerializerMethodField('get_subtotal')
	oferta = serializers.SerializerMethodField('get_oferta')
	class Meta:
		model = LineaCarro
		fields = ('id','carro','producto','variacion','cantidad','thum','nombre','talla','precio','subtotal','oferta')

	def get_thum(self,obj):
		thum = obj.producto.get_thum().url
		return thum

	def get_nombre(self,obj):
		return obj.producto.full_name

	def get_talla(self,obj):
		return obj.variacion.talla

	def get_precio(self,obj):
		precio = obj.variacion.get_precio_venta()
		return "%0.2f" %(precio)

	def get_subtotal(self,obj):
		subtotal = obj.get_subtotal()
		return "%0.2f" %(subtotal)

	def get_oferta(self,obj):
		return obj.variacion.oferta