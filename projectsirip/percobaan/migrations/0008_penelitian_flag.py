# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0007_auto_20170619_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='penelitian',
            name='flag',
            field=models.SmallIntegerField(default=1, choices=[(1, b'Draft'), (2, b'Publish')]),
            preserve_default=False,
        ),
    ]
