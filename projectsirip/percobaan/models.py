    # -*- coding: utf-8 -*-

# Create your models here.
from django.db import models

class Authors(models.Model):
    class Meta:
        verbose_name_plural = 'Authors'
    authors= models.CharField(max_length=100,unique=True)

    def __unicode__(self):
        return self.authors

class Role(models.Model):
    class Meta:
        verbose_name_plural = 'Role'
    role = models.SmallIntegerField(choices=(
        (1, 'Dosen'),
        (2, 'Mahasiswa'),
        (3, 'Staff')
    ))

    def __unicode__(self):
        return self.get_role_display()

class Fokus_Penelitian(models.Model):

    class Meta:
        verbose_name_plural = 'Fokus Penelitian'

    nama = models.CharField(max_length=100, primary_key=True)
    parent = models.ForeignKey('Fokus_Penelitian', on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return self.nama

class Fakultas(models.Model):
    class Meta:
        verbose_name_plural = 'Fakultas'
    fakultas = models.CharField(max_length=100, primary_key=True)

    def __unicode__(self):
        return self.fakultas

class Program_Studi(models.Model):

    class Meta:
        verbose_name_plural = 'Program Studi'
    nama_fakultas = models.ForeignKey(Fakultas, on_delete=models.CASCADE, default='SOME STRING')
    program_studi = models.CharField(max_length=100)

    def __unicode__(self):
        return self.program_studi

class Asal_Sumber_Dana(models.Model):

    class Meta:
        verbose_name_plural = 'Asal Sumber Dana'
    sumber_dana = models.CharField(max_length=50, primary_key=True)

    def __unicode__(self):
        return self.sumber_dana

class User(models.Model):

    class Meta:
        verbose_name_plural = 'User'
    username = models.CharField(max_length=50)
    nama = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nama

class Jenis_Penelitian(models.Model):

    class Meta:
        verbose_name_plural = 'Jenis Penelitian'
    nama_jenis_penelitian = models.CharField(max_length=100)
    deskripsi = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nama_jenis_penelitian

class pemerintah(models.Model):
    class Meta:
        verbose_name_plural = 'pemerintah'
    instansi = models.CharField(max_length=100)

    def __unicode__(self):
        return self.instansi

class Penelitian(models.Model):

    class Meta:
        verbose_name_plural = 'Penelitian'
    judul_penelitian = models.CharField(max_length=500)
    nomor_kontrak = models.CharField(max_length=100)
    tahun_pelaksanaan = models.PositiveSmallIntegerField()
    jenis_penelitian = models.ForeignKey(Jenis_Penelitian, on_delete=models.CASCADE)
    bidang_penelitian = models.ForeignKey(Fokus_Penelitian,on_delete=models.CASCADE)
    asal_sumber_dana = models.ManyToManyField(Asal_Sumber_Dana)
    jenis_sumber_dana = models.CharField(max_length=50)
    nama_sumber_dana = models.CharField(max_length=100)
    jumlah_dana_dalam_negeri = models.DecimalField(max_digits=12,decimal_places=2)
    jumlah_dana_luar_negeri = models.DecimalField(max_digits=12,decimal_places=2)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.SmallIntegerField(choices=(
        (1, 'Valid'),
        (2, 'Tidak Valid'),
        (3, 'Belum diverifikasi')
    ))
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    flag = models.SmallIntegerField(choices=(
        (1, 'Draft'),
        (2, 'Publish')
    ))

    def __unicode__(self):
        return self.judul_penelitian

class Penelitian_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    judul_penelitian = models.ForeignKey(Penelitian,related_name='+',default='judul')

    def __unicode__(self):
        return self.authors_id
