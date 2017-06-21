# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0011_auto_20170620_0541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penelitian',
            name='status_data',
            field=models.SmallIntegerField(choices=[(1, b'Valid'), (2, b'Tidak Valid'), (3, b'Belum diverifikasi')]),
        ),
    ]