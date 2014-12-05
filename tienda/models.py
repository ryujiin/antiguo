from django.db import models
from django.template.defaultfilters import slugify
from catalogo.models import Categoria


class Menu(models.Model):
	nombre = models.CharField(max_length=120,blank=True,null=True)
	bloque = models.ForeignKey('Bloque',blank=True,null=True)

class Bloque(models.Model):
	nombre = models.CharField(max_length=120,blank=True,null=True)
	pagina = models.ForeignKey('Pagina',blank=True,null=True)
	activo = models.BooleanField(default=True)
	cuerpo = models.TextField(blank=True,null=True)

class Pagina(models.Model):
	titulo = models.CharField(max_length=120,blank=True,null=True)
	slug = models.CharField(max_length=120,unique=True,blank=True,null=True)
	menu = models.ForeignKey('Menu')
	activo = models.BooleanField(default=True)
	cuerpo = models.TextField(blank=True,null=True)

