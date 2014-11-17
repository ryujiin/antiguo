# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_productoimagen_orden'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productoimagen',
            options={'ordering': ['orden']},
        ),
    ]
