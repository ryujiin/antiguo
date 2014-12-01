# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0007_auto_20141201_0253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='genero',
        ),
        migrations.AddField(
            model_name='categoria',
            name='genero',
            field=models.ForeignKey(blank=True, to='catalogo.Genero', null=True),
            preserve_default=True,
        ),
    ]
