# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0008_auto_20141201_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='banner',
            field=models.ImageField(max_length=250, null=True, upload_to=b'categories/banner/', blank=True),
            preserve_default=True,
        ),
    ]
