# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description', models.TextField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('seats', models.IntegerField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Institutions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('x_coord', models.TextField()),
                ('y_coord', models.TextField()),
            ],
        ),
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
        migrations.AddField(
            model_name='event',
            name='institution',
            field=models.ForeignKey(to='myapp.Institutions'),
        ),
        migrations.AddField(
            model_name='comments',
            name='event',
            field=models.ForeignKey(to='myapp.Event'),
        ),
        migrations.AddField(
            model_name='comments',
            name='institution',
            field=models.ForeignKey(to='myapp.Institutions'),
        ),
    ]
