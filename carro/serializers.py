from rest_framework import serializers
from models import *
from django.conf import settings

class CarroSerializer(serializers.ModelSerializer):
	lineas = serializers.SerializerMethodField('get_lineas')

	class Meta:
		model = Carro
		fields = ('id','propietario','estado','sesion_carro','lineas')

	def get_lineas(self,obj):
		return obj.num_lineas()

class LineaSerializer(serializers.ModelSerializer):
	class Meta:
		model = LineaCarro

