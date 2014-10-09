# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
                ('full_name', models.CharField(max_length=255, editable=False, db_index=True)),
                ('slug', models.SlugField(unique=True, max_length=120, editable=False)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('imagen', models.ImageField(max_length=250, null=True, upload_to=b'categories', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Estilo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, null=True, blank=True)),
                ('full_name', models.CharField(max_length=120, unique=True, null=True, editable=False, blank=True)),
                ('marca', models.CharField(max_length=120, choices=[(b'Loviz DelCarpio', b'Loviz DelCarpio'), (b'Doomckan DC', b'Doomckan DC')])),
                ('slug', models.CharField(max_length=120, editable=False)),
                ('activo', models.BooleanField(default=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to=b'uploads/catalogo/producto/imagen/')),
                ('categoria', models.ForeignKey(blank=True, to='catalogo.Categoria', null=True)),
                ('color', models.ForeignKey(blank=True, to='catalogo.Color', null=True)),
                ('estilo', models.ForeignKey(blank=True, to='catalogo.Estilo', null=True)),
                ('parientes', models.ManyToManyField(related_name='parientes_rel_+', null=True, to='catalogo.Producto', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='categoria',
            name='seccion',
            field=models.ForeignKey(to='catalogo.Seccion'),
            preserve_default=True,
        ),
    ]
