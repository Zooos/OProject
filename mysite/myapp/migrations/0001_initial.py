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
                ('description', models.TextField()),
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
