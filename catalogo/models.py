from django.db import models
from django.template.defaultfilters import slugify
from sorl.thumbnail import get_thumbnail
from django.conf import settings

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

		url ="%s%s" %(settings.S3_URL,img.name)
		return url

	def get_en_oferta(self):
		variaciones = self.get_variaciones()
		for varia in variaciones:
			if varia.oferta != 0:
				return True
		return False

	def get_variaciones(self):
		variaciones = ProductoVariacion.objects.filter(producto=self).order_by('-oferta')
		return variaciones

	def get_precio_lista(self):
		en_oferta = self.get_en_oferta()
		if en_oferta:
			variaciones=self.get_variaciones()
		else:
			variaciones = ProductoVariacion.objects.filter(producto=self).order_by('-precio_minorista')
		if variaciones:
			precio = variaciones[0].precio_minorista
		else:
			precio = 0
		return precio

	def get_precio_oferta_lista(self):
		en_oferta = self.get_en_oferta()
		if en_oferta:
			variaciones=self.get_variaciones()
			precio = variaciones[0].precio_minorista
			oferta = variaciones[0].oferta
			descuento= precio*oferta/100
			precio = precio - descuento
		else:
			precio = 0
		return precio
			

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

class ProductoVariacion(models.Model):
	producto = models.ForeignKey(Producto,related_name='variaciones')
	talla = models.ForeignKey(Talla)
	precio_minorista = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	oferta = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "%s-%s" %(self.producto,self.precio_minorista)

class ProductoImagen(models.Model):
	producto = models.ForeignKey(Producto,related_name="imagenes_producto")
	foto = models.ImageField(upload_to="catalogo/producto/imagen/")
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)