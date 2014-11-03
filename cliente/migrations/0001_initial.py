# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('apellido', models.CharField(max_length=100, null=True, blank=True)),
                ('genero', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Hombre', b'hombre'), (b'Mujer', b'mujer')])),
                ('dni', models.CharField(max_length=10, null=True, blank=True)),
                ('usuario', models.ForeignKey(related_name=b'cliente', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento', models.CharField(max_length=100, null=True, blank=True)),
                ('provincia', models.CharField(max_length=100, null=True, blank=True)),
                ('distrito', models.CharField(max_length=100, null=True, blank=True)),
                ('usuario', models.ForeignKey(related_name=b'usuario', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
