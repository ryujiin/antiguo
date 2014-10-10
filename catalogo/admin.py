from django.contrib import admin
from models import *
# Register your models here.

class ProductoImagenInline(admin.TabularInline):
	model = ProductoImagen

class VariacionInline(admin.TabularInline):
	model = ProductoVariacion

class ProductoAdmin(admin.ModelAdmin):
	inlines = [ProductoImagenInline,VariacionInline]
	list_display = ('id','full_name','nombre','slug','get_en_oferta','get_variaciones','get_precio_lista','get_precio_oferta_lista')


admin.site.register(Producto,ProductoAdmin)
admin.site.register(Color)
admin.site.register(Talla)
admin.site.register(Categoria)
admin.site.register(Seccion)
admin.site.register(Estilo)