# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0004_auto_20170619_0642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='penelitian',
            old_name='institusi_sumber_dana',
            new_name='nama_sumber_dana',
        ),
        migrations.RemoveField(
            model_name='penelitian',
            name='nama_institusi_sumber_dana',
        ),
        migrations.AddField(
            model_name='penelitian',
            name='jenis_sumber_dana',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
