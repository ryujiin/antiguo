from django.db import models
from django.template.defaultfilters import slugify
from sorl.thumbnail import get_thumbnail

# Create your models here.
class Producto(models.Model):
	MARCAS = (
    ('Loviz DelCarpio', 'Loviz DelCarpio'),
    ('Doomckan DC', 'Doomckan DC'),
)
	nombre = models.CharField(max_length=120,blank=True,null=True)
	full_name = models.CharField(max_length=120, unique=True,blank=True,null=True,editable=False)
	marca = models.CharField(max_length=120, choices=MARCAS)
	categoria = models.ForeignKey('Categoria',blank=True,null=True,related_name='cate')
	estilo = models.ForeignKey('Estilo',blank=True,null=True)
	color = models.ForeignKey('Color',blank=True,null=True,)
	slug = models.CharField(max_length=120,editable=False)
	parientes = models.ManyToManyField('self',blank=True,null=True, related_name='colores')
	activo = models.BooleanField(default=True)
	descripcion = models.TextField(blank=True,null=True)
	creado = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField(upload_to="uploads/catalogo/producto/imagen/")

	def __unicode__(self):
		return self.full_name

	def save(self, *args, **kwargs):
		self.full_name = ("%s %s (%s)") %(self.categoria,self.nombre,self.color)
		if not self.slug:
			self.slug = slugify(self.full_name)
		super(Producto, self).save(*args, **kwargs)

	def get_thum(self):
		img = get_thumbnail(self.imagen, '160x100', quality=99)
		#img = self.imagen.url
		return img

class Color(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Talla(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Categoria(models.Model):
	nombre = models.CharField(max_length=120)
	seccion = models.ForeignKey('Seccion')
	full_name = models.CharField(max_length=255,db_index=True, editable=False)
	slug = models.SlugField(max_length=120,unique=True,editable=False)
	descripcion = models.TextField(blank=True,null=True)
	activo = models.BooleanField(default=True)
	imagen = models.ImageField(upload_to='categories',blank=True,null=True,max_length=250)
	
	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.full_name:
			self.full_name = ('%s - %s') %(self.seccion,self.nombre)
		super(Categoria, self).save(*args, **kwargs)

class Seccion(models.Model):
	nombre = models.CharField(max_length=120)

	def __unicode__(self):
		return self.nombre

class Estilo(models.Model):
	nombre = models.CharField(max_length=120)

	def __unicode__(self):
		return self.nombre
    