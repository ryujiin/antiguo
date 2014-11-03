# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_auto_20141102_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='codigo_postal',
            field=models.CharField(max_length=20, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(related_name=b'direcciones', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
