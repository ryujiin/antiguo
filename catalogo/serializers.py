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
	genero = serializers.SerializerMethodField('get_genero')
	class Meta:
		model=Producto
		fields =('id','nombre','full_name','marca','categoria','estilo','genero','color','slug','activo','thum','en_oferta','precio','precio_mostrar')

	def get_img_thum(self,obj):
		img = obj.get_thum().url
		return img

	def get_oferta(self,obj):
		return obj.get_en_oferta

	def get_precio(self,obj):
		return obj.get_precio_lista

	def get_precio_descuento(self,obj):
		return obj.get_precio_oferta_lista

	def get_genero(self,obj):
		return obj.categoria.genero.slug

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
	imagen_medium = serializers.SerializerMethodField('get_imagen_medium')
	imagen_thum = serializers.SerializerMethodField('get_imagen_thum')
	class Meta:
		model = ProductoImagen
		fields =('imagen','imagen_medium','imagen_thum','orden')
	
	def get_imagen(self,obj):
		return obj.foto.url

	def get_imagen_medium(self,obj):
		url = obj.get_thum_medium().url
		return url

	def get_imagen_thum(self,obj):
		url = obj.get_thum().url
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
	categoria= serializers.CharField(read_only=True)
	estilo= serializers.CharField(read_only=True)
	color= serializers.CharField(read_only=True)
	variaciones = ProductoVariacionSerializer(many=True)
	imagenes_producto = ImgProductoSerializer(many=True)
	thum = serializers.SerializerMethodField('get_thum')
	variaciones = ProductoVariacionSerializer(many=True)
	parientes = ParienteSerialiezer(many=True)

	en_oferta = serializers.SerializerMethodField('get_oferta')
	precio = serializers.SerializerMethodField('get_precio')
	precio_venta = serializers.SerializerMethodField('get_precio_descuento')

	class Meta:
		model = Producto
		fields = ('id','nombre','full_name','marca','categoria','estilo','color','slug','activo','descripcion','thum',
				'en_oferta','precio','precio_venta',
				'imagenes_producto','variaciones','parientes')

	def get_thum(self,obj):
		thum = obj.get_thum().url
		return thum

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

class CategoriaSerializer(serializers.ModelSerializer):
	genero = serializers.CharField(read_only=True)
	seccion = serializers.CharField(read_only=True)
	imagen = serializers.SerializerMethodField('get_imagen')
	banner = serializers.SerializerMethodField('get_banner')
	genero_slug = serializers.SerializerMethodField('get_genero_slug')

	class Meta:
		model = Categoria
		fields = ('id','nombre','slug','genero','genero_slug','activo','imagen','descripcion','full_name','seccion','banner')

	def get_banner(self,obj):
		if obj.banner:
			return obj.banner.url

	def get_imagen(self,obj):
		if obj.imagen:
			return obj.imagen.url

	def get_genero_slug(self,obj):
		return obj.genero.slug
