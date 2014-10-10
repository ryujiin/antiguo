from rest_framework import serializers
from models import *
from django.conf import settings

class ProductoListaSerializer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField('get_img_thum')
	categoria= serializers.CharField(read_only=True)
	estilo= serializers.CharField(read_only=True)
	color= serializers.CharField(read_only=True)
	en_oferta = serializers.SerializerMethodField('get_oferta')
	precio = serializers.SerializerMethodField('get_precio')
	precio_mostrar = serializers.SerializerMethodField('get_precio_descuento')
	class Meta:
		model=Producto
		fields =('id','nombre','full_name','marca','categoria','estilo','color','slug','activo','thum','en_oferta','precio','precio_mostrar')

	def get_img_thum(self,obj):
		img = obj.get_thum
		return img

	def get_oferta(self,obj):
		return obj.get_en_oferta

	def get_precio(self,obj):
		return obj.get_precio_lista

	def get_precio_descuento(self,obj):
		return obj.get_precio_oferta_lista