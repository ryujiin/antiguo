from django.db import models
from django.template.defaultfilters import slugify
from catalogo.models import Categoria


# Create your models here.
class Menu_principal(models.Model):
	nombre = models.CharField(max_length=120,blank=True,null=True)
	slug = models.CharField(max_length=120,editable=True)
	activo = models.BooleanField(default=True)
	orden = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return self.nombre