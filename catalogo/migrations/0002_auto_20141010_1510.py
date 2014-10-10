# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoImagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foto', models.ImageField(upload_to=b'catalogo/producto/imagen/')),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('producto', models.ForeignKey(related_name=b'imagenes_producto', to='catalogo.Producto')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductoVariacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('precio_minorista', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('oferta', models.PositiveIntegerField(default=0)),
                ('producto', models.ForeignKey(related_name=b'variaciones', to='catalogo.Producto')),
                ('talla', models.ForeignKey(to='catalogo.Talla')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(related_name=b'cate', blank=True, to='catalogo.Categoria', null=True),
        ),
    ]
