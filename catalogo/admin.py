from django.contrib import admin
from models import *
# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
	list_display = ('id','full_name','nombre','slug')

admin.site.register(Producto,ProductoAdmin)
admin.site.register(Color)
admin.site.register(Talla)
admin.site.register(Categoria)
admin.site.register(Seccion)
admin.site.register(Estilo)