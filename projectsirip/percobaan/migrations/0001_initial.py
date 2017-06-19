# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asal_Sumber_Dana',
            fields=[
                ('sumber_dana', models.CharField(max_length=50, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('authors', models.CharField(unique=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fakultas',
            fields=[
                ('fakultas', models.CharField(max_length=100, serialize=False, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fokus_Penelitian',
            fields=[
                ('nama', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('parent', models.ForeignKey(to='percobaan.Fokus_Penelitian')),
            ],
        ),
        migrations.CreateModel(
            name='Jenis_Penelitian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nama_jenis_penelitian', models.CharField(max_length=100)),
                ('deskripsi', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Penelitian',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('judul_penelitian', models.CharField(max_length=500)),
                ('nomor_kontrak', models.CharField(max_length=100)),
                ('tahun_pelaksanaan', models.PositiveSmallIntegerField()),
                ('jenis_sumber_dana', models.CharField(max_length=50)),
                ('nama_sumber_dana', models.CharField(max_length=100)),
                ('institusi_sumber_dana', models.CharField(max_length=100)),
                ('nama_institusi_sumber_dana', models.CharField(max_length=100)),
                ('jumlah_dana_dalam_negeri', models.DecimalField(max_digits=12, decimal_places=2)),
                ('jumlah_dana_luar_negeri', models.DecimalField(max_digits=12, decimal_places=2)),
                ('status_data', models.CharField(max_length=100)),
                ('file_path', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now=True)),
                ('asal_sumber_dana', models.ManyToManyField(to='percobaan.Asal_Sumber_Dana')),
                ('bidang_penelitian', models.ForeignKey(to='percobaan.Fokus_Penelitian')),
                ('jenis_penelitian', models.ForeignKey(to='percobaan.Jenis_Penelitian')),
            ],
        ),
        migrations.CreateModel(
            name='Penelitian_Authors_Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=50)),
                ('authors', models.ForeignKey(to='percobaan.Authors', to_field=b'authors')),
                ('judul_penelitian', models.ForeignKey(related_name='+', default=b'judul', to='percobaan.Penelitian')),
            ],
        ),
        migrations.CreateModel(
            name='Program_Studi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('program_studi', models.CharField(max_length=100)),
                ('nama_fakultas', models.ForeignKey(default=b'SOME STRING', to='percobaan.Fakultas')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='penelitian',
            name='penginput',
            field=models.ForeignKey(to='percobaan.User'),
        ),
        migrations.AddField(
            model_name='penelitian',
            name='program_studi',
            field=models.ForeignKey(to='percobaan.Program_Studi'),
        ),
    ]
