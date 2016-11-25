# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('categoria', models.ForeignKey(to='blog.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('preciomin', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('foto', models.ImageField(upload_to='media/fotos/')),
                ('categoriast', models.ManyToManyField(to='blog.Categoria', through='blog.Categorias')),
                ('precentaciones', models.ManyToManyField(to='blog.Presentacion', through='blog.Precio')),
            ],
        ),
        migrations.AddField(
            model_name='precio',
            name='presentacion',
            field=models.ForeignKey(to='blog.Presentacion'),
        ),
        migrations.AddField(
            model_name='precio',
            name='producto',
            field=models.ForeignKey(to='blog.Producto'),
        ),
        migrations.AddField(
            model_name='categorias',
            name='producto',
            field=models.ForeignKey(to='blog.Producto'),
        ),
    ]
