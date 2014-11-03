# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0003_auto_20141103_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='direccion',
            name='tipo',
            field=models.CharField(blank=True, max_length=100, null=True, choices=[(b'envio', b'Direccion de envio'), (b'facturacion', b'Direccion de Facturacion')]),
            preserve_default=True,
        ),
    ]
