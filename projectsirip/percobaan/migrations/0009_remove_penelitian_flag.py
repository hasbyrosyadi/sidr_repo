# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0008_penelitian_flag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='penelitian',
            name='flag',
        ),
    ]
