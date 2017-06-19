# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fokus_penelitian',
            name='parent',
            field=models.ForeignKey(blank=True, to='percobaan.Fokus_Penelitian', null=True),
        ),
    ]
