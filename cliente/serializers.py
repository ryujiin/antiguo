from models import *
from rest_framework import serializers
from django.contrib.auth.models import User as User


class DireccionSerilizer(serializers.ModelSerializer):
	class Meta:
		model = Direccion

class UsuarioSerializer(serializers.ModelSerializer):
	class Meta:
		model = User

class PerfilUSerSerializer(serializers.ModelSerializer):
	email = serializers.SerializerMethodField('get_email')
	nombre = serializers.SerializerMethodField('get_nombre')
	apellido = serializers.SerializerMethodField('get_apellido')

	direcciones = DireccionSerilizer(many=True)
	class Meta:
		model = Cliente
		fields = ('id','usuario','nombre','apellido','email','dni','telefono','direcciones')

	def get_email(self,obj):
		return obj.usuario.email

	def get_nombre(self,obj):
		return obj.usuario.first_name

	def get_apellido(self,obj):
		return obj.usuario.last_name