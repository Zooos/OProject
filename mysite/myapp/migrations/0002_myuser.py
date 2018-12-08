# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=20)),
                ('gender', models.BooleanField()),
                ('age', models.IntegerField()),
                ('institution', models.ManyToManyField(to='myapp.Institutions')),
            ],
        ),
    ]
