# -*- coding: utf-8 -*-

# Create your models here.
from django.db import models

class Authors(models.Model):
    authors= models.CharField(max_length=100,unique=True)

class Role(models.Model):
    role = models.CharField(max_length=50)

class Fokus_Penelitian(models.Model):
    major = models.CharField(max_length=100, primary_key=True)
    minor = models.CharField(max_length=100)

class Fakultas(models.Model):
    fakultas = models.CharField(max_length=100, primary_key=True)

class Program_Studi(models.Model):
    nama_fakultas = models.ForeignKey(Fakultas, on_delete=models.CASCADE, default='SOME STRING')
    program_studi = models.CharField(max_length=100)

class Table_Asal_Sumber_Dana(models.Model):
    sumber_dana = models.CharField(max_length=50, primary_key=True)

class Table_Relasi_Asal_Sumber_Dana(models.Model):
    relasi = models.ManyToManyField(Table_Asal_Sumber_Dana)

class User(models.Model):
    username = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)

class Jenis_Penelitian(models.Model):
    nama_jenis_penelitian = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=200)

class Penelitian(models.Model):
    judul_penelitian = models.CharField(max_length=500)
    nomor_kontrak = models.CharField(max_length=100)
    tahun_pelaksanaan = models.PositiveSmallIntegerField()
    jenis_penelitian = models.ForeignKey(Jenis_Penelitian, on_delete=models.CASCADE)
    bidang_penelitian = models.ForeignKey(Fokus_Penelitian,on_delete=models.CASCADE)
    asal_sumber_dana = models.ForeignKey(Table_Relasi_Asal_Sumber_Dana, on_delete=models.CASCADE)
    jenis_sumber_dana=models.CharField(max_length=50)
    nama_sumber_dana = models.CharField(max_length=100)
    institusi_sumber_dana = models.CharField(max_length=100)
    nama_institusi_sumber_dana = models.CharField(max_length=100)
    jumlah_dana_dalam_negeri = models.DecimalField(max_digits=12,decimal_places=2)
    jumlah_dana_luar_negeri = models.DecimalField(max_digits=12,decimal_places=2)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)

class Penelitian_Authors_Role(models.Model):

    role = models.CharField(max_length=50)
    authors = models.ForeignKey(Authors,to_field='authors')
    judul_penelitian = models.ForeignKey(Penelitian,related_name='+',default='judul')
