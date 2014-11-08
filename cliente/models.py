from django.db import models
from django.contrib.auth.models import User as User

# Create your models here.
class Cliente(models.Model):
	GENEROS = (('Hombre','hombre'),('Mujer','mujer'),)
	usuario = models.ForeignKey(User,related_name='cliente', null=True,blank=True,unique=True)
	genero = models.CharField(max_length=100,blank=True,null=True,choices=GENEROS)
	dni = models.CharField(max_length=10,blank=True,null=True)
	telefono = models.CharField(max_length=11,blank=True,null=True)
    
class Direccion(models.Model):
	TIPO = (('envio','Direccion de envio'),('facturacion','Direccion de Facturacion'))
	usuario = models.ForeignKey(User,related_name='direcciones', null=True,blank=True)
	tipo = models.CharField(max_length=100,blank=True,null=True,choices=TIPO)
	departamento = models.CharField(max_length=100,blank=True,null=True)
	provincia = models.CharField(max_length=100,blank=True,null=True)
	distrito = models.CharField(max_length=100,blank=True,null=True)
	direccion = models.CharField(max_length=100,blank=True,null=True)
	codigo_postal = models.CharField(max_length=20,blank=True,null=True)
