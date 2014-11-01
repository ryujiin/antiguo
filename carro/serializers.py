from rest_framework import serializers
from models import *
from django.conf import settings

class CarroSerializer(serializers.ModelSerializer):
	class Meta:
		model = Carro