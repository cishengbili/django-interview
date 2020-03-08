# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_number', models.CharField(unique=True, max_length=50)),
                ('point', models.IntegerField()),
            ],
            options={
                'db_table': 'player_point',
            },
            bases=(models.Model,),
        ),
    ]
