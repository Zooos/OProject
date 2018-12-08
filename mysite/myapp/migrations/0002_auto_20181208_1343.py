# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('event', models.ForeignKey(to='myapp.Event')),
            ],
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='institution',
        ),
        migrations.AddField(
            model_name='userevent',
            name='user',
            field=models.ForeignKey(to='myapp.MyUser'),
        ),
    ]
