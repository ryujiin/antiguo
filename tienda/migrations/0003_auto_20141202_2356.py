# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20141202_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloque',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('cuerpo', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, null=True, blank=True)),
                ('bloque', models.ForeignKey(blank=True, to='tienda.Bloque', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=120, null=True, blank=True)),
                ('slug', models.CharField(max_length=120, unique=True, null=True, blank=True)),
                ('activo', models.BooleanField(default=True)),
                ('cuerpo', models.TextField(null=True, blank=True)),
                ('menu', models.ForeignKey(to='tienda.Menu')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Menu_principal',
        ),
        migrations.AddField(
            model_name='bloque',
            name='pagina',
            field=models.ForeignKey(blank=True, to='tienda.Pagina', null=True),
            preserve_default=True,
        ),
    ]
