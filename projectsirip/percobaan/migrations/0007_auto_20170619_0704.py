# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0006_pemerintah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='penelitian_authors_role',
            name='role',
            field=models.ForeignKey(to='percobaan.Role'),
        ),
    ]
