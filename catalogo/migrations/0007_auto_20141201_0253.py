# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0006_auto_20141129_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='slug',
            field=models.SlugField(null=True, editable=False, max_length=120, blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='estilo',
            name='slug',
            field=models.SlugField(null=True, editable=False, max_length=120, blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='genero',
            name='slug',
            field=models.SlugField(null=True, editable=False, max_length=120, blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='seccion',
            name='slug',
            field=models.SlugField(null=True, editable=False, max_length=120, blank=True, unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='talla',
            name='slug',
            field=models.SlugField(null=True, editable=False, max_length=120, blank=True, unique=True),
            preserve_default=True,
        ),
    ]
