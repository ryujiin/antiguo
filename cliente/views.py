from django.shortcuts import render
from models import *
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from serializers import PerfilUSerSerializer,UsuarioSerializer
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import viewsets
from django.http import HttpResponse, Http404



# Create your views here.

class PerfilUserViewSet(APIView):
	permission_classes = (IsAuthenticated,)

	def get_object(self):
		try:
			return Cliente.objects.get(usuario=self.request.user)
		except Cliente.DoesNotExist:
			raise Http404

	def get(self,request,format=None):
		perfil = self.get_object()
		serializer = PerfilUSerSerializer(perfil)
		return Response(serializer.data)

class UsuarioViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAdminUser,)
	model = User
	serializer_class = UsuarioSerializer