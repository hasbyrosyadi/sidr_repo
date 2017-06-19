# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('percobaan', '0002_auto_20170619_0606'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asal_sumber_dana',
            options={'verbose_name_plural': 'Asal Sumber Dana'},
        ),
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='fakultas',
            options={'verbose_name_plural': 'Fakultas'},
        ),
        migrations.AlterModelOptions(
            name='fokus_penelitian',
            options={'verbose_name_plural': 'Fokus Penelitian'},
        ),
        migrations.AlterModelOptions(
            name='jenis_penelitian',
            options={'verbose_name_plural': 'Jenis Penelitian'},
        ),
        migrations.AlterModelOptions(
            name='penelitian',
            options={'verbose_name_plural': 'Penelitian'},
        ),
        migrations.AlterModelOptions(
            name='penelitian_authors_role',
            options={'verbose_name_plural': 'Author Role'},
        ),
        migrations.AlterModelOptions(
            name='program_studi',
            options={'verbose_name_plural': 'Program Studi'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name_plural': 'Role'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name_plural': 'User'},
        ),
        migrations.AlterField(
            model_name='role',
            name='role',
            field=models.SmallIntegerField(choices=[(1, b'Dosen'), (2, b'Mahasiswa'), (3, b'Staff')]),
        ),
    ]
