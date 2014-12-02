# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0010_auto_20141202_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='slug',
            field=models.CharField(max_length=120, unique=True, null=True, blank=True),
        ),
    ]
