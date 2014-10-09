from rest_framework import serializers
from models import *
from django.conf import settings

class ProductoListaSerializer(serializers.ModelSerializer):
	thum = serializers.SerializerMethodField('get_img_thum')
	categoria= serializers.CharField(read_only=True)
	estilo= serializers.CharField(read_only=True)
	color= serializers.CharField(read_only=True)
	class Meta:
		model=Producto
		fields =('id','nombre','full_name','marca','categoria','estilo','color','slug','activo','thum',)

	def get_img_thum(self,obj):
		img = obj.get_thum
		return img