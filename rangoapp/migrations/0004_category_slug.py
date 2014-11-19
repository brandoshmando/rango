# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rangoapp', '0003_auto_20141118_0116'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2014, 11, 18, 23, 48, 54, 403344, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
