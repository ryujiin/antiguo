# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0004_direccion_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(related_name=b'direcciones', blank=True, to='cliente.Cliente', null=True),
        ),
    ]
