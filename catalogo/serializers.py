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

class ProductoVariacionSerializer(serializers.ModelSerializer):
	talla = serializers.CharField(read_only=True)
	precio_venta = serializers.SerializerMethodField('get_precio')
	precio = serializers.SerializerMethodField('get_precio_minorista')
	class Meta:
		model=ProductoVariacion
		fields =('id','talla','precio','oferta','precio_venta')

	def get_precio(self,obj):
		return obj.get_precio_venta()
	def get_precio_minorista(self,obj):
		precio = obj.precio_minorista
		precio ="%0.2f" %(precio)
		return precio


class ImgProductoSerializer(serializers.ModelSerializer):
	imagen = serializers.SerializerMethodField('get_imagen')
	class Meta:
		model = ProductoImagen
		fields =('imagen',)
		
	def get_imagen(self,obj):
		url = "%s%s" %(settings.S3_URL,obj.foto.name)
		return url

class ParienteSerialiezer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField('get_img_thum')
	class Meta:
		model = Producto
		fields = ('id','nombre','full_name','marca','thum','slug')

	def get_img_thum(self,obj):
		img = obj.get_thum
		return img

class ProductoSingleSereializer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField('get_img_thum')
	categoria= serializers.CharField(read_only=True)
	estilo= serializers.CharField(read_only=True)
	color= serializers.CharField(read_only=True)
	imagen_p = serializers.SerializerMethodField('get_imagen_aws')
	imagenes_producto = ImgProductoSerializer(many=True)
	variaciones = ProductoVariacionSerializer(many=True)

	parientes = ParienteSerialiezer(many=True)

	en_oferta = serializers.SerializerMethodField('get_oferta')
	precio = serializers.SerializerMethodField('get_precio')
	precio_venta = serializers.SerializerMethodField('get_precio_descuento')

	class Meta:
		model = Producto
		fields =('id','nombre','full_name','marca','categoria',
			     'thum','estilo','color','slug','activo','imagen_p',
			     'descripcion','imagenes_producto','variaciones','parientes','en_oferta','precio','precio_venta')
	
	def get_imagen_aws(self,obj):
		url = "%s%s" %(settings.S3_URL,obj.imagen.name)
		return url

	def get_img_thum(self,obj):
		img = obj.get_thum
		return img

	def get_oferta(self,obj):
		return obj.get_en_oferta

	def get_precio(self,obj):
		precio= obj.get_precio_lista()
		precio ="%0.2f" %(precio)
		return precio

	def get_precio_descuento(self,obj):
		precio= obj.get_precio_oferta_lista()
		precio ="%0.2f" %(precio)
		return precio
