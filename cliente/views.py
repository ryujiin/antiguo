from django.shortcuts import render
from models import *
from serializers import PerfilUSerSerializer,UsuarioSerializer,UserSerializer
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework import authentication, permissions, parsers, renderers
from rest_framework import viewsets, generics
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view, throttle_classes
from social.apps.django_app.utils import psa

from django.http import HttpResponse, Http404
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class PerfilUserViewSet(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self,request,format=None):
		try:
			perfil = User.objects.get(pk=request.user.pk)
		except User.DoesNotExist:
			raise Http404

		serializer = UsuarioSerializer(perfil)
		return Response(serializer.data)

from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrTargetUser

class UsuarioViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	model = User

	def get_permissions(self):
		return (AllowAny() if self.request.method == 'POST'
			else IsStaffOrTargetUser()),


@csrf_exempt
@psa('social:complete')
def register_by_access_token(request, backend):
	token = request.GET.get('access_token')
	backend = request.backend
	user = backend.do_auth(token)
	return user


class ObtainAuthToken(APIView):
	throttle_classes = ()
	permission_classes = ()
	parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
	renderer_classes = (renderers.JSONRenderer,)
	serializer_class = AuthTokenSerializer
	model = Token
	
	# Accept backend as a parameter and 'auth' for a login / pass
	def post(self, request, backend):
		serializer = self.serializer_class(data=request.DATA)

			# Here we call PSA to authenticate like we would if we used PSA on server side.
		user = register_by_access_token(request, backend)
		if user:
			login(request, user)

		# If user is active we get or create the REST token and send it back with user data
		if user and user.is_active:
			token, created = Token.objects.get_or_create(user=user)
			return Response({'id': user.id , 'name': user.username, 'userRole': 'user','token': token.key})

