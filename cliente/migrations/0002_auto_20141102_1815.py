# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='nombre',
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=11, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='direccion',
            name='direccion',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(related_name=b'cliente', null=True, blank=True, to=settings.AUTH_USER_MODEL, unique=True),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(related_name=b'usuario', null=True, blank=True, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
