# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20141031_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoimagen',
            name='orden',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]
