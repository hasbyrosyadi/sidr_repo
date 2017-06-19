# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0003_auto_20170619_0625'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penelitian',
            name='jenis_sumber_dana',
        ),
        migrations.RemoveField(
            model_name='penelitian',
            name='nama_sumber_dana',
        ),
    ]
