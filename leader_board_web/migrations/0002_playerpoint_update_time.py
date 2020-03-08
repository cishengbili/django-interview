# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('leader_board_web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playerpoint',
            name='update_time',
            field=models.DateField(default=datetime.datetime(2020, 3, 8, 7, 3, 21, 528745), auto_now=True),
            preserve_default=False,
        ),
    ]
