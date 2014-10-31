# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import catalogo.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20141010_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoimagen',
            name='foto',
            field=models.ImageField(upload_to=catalogo.models.url_imagen_pr),
        ),
    ]
