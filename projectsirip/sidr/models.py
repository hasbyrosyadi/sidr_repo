    # -*- coding: utf-8 -*-

# Create your models here.

from django.core.validators import FileExtensionValidator
from django.db import models


class Authors(models.Model):
    class Meta:
        verbose_name_plural = 'Authors'
    authors= models.CharField(max_length=100,unique=True)

    def __unicode__(self):
        return self.authors

class Anggota(models.Model):
    class Meta:
        verbose_name_plural = 'Anggota'
    username = models.CharField(max_length=100,primary_key=True)
    nip = models.CharField(max_length=100)
    nama = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nama

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
    parent = models.ForeignKey('Fokus_Penelitian', null=True, blank=True, related_name='anak')

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
    nama_fakultas = models.ForeignKey(Fakultas, default='SOME STRING')
    program_studi = models.CharField(max_length=100)

    def __unicode__(self):
        return self.program_studi

class Asal_Sumber_Dana(models.Model):

    class Meta:
        verbose_name_plural = 'Asal Sumber Dana'
    sumber_dana = models.CharField(max_length=50)

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
    deskripsi = models.CharField(max_length=500)

    def __unicode__(self):
        return self.nama_jenis_penelitian

class Pemerintah(models.Model):
    class Meta:
        verbose_name_plural = 'pemerintah'
    instansi = models.CharField(max_length=100)

    def __unicode__(self):
        return self.instansi

class Penelitian(models.Model):
    judul_penelitian = models.CharField(max_length=500)
    nomor_kontrak = models.CharField(max_length=100)
    tahun_pelaksanaan = models.DateField(null=True, blank=True)
    jenis_penelitian = models.ForeignKey(Jenis_Penelitian)
    bidang_penelitian = models.ForeignKey(Fokus_Penelitian)
    asal_sumber_dana = models.ManyToManyField(Asal_Sumber_Dana)
    jenis_sumber_dana = models.ForeignKey(Pemerintah)
    nama_sumber_dana = models.CharField(max_length=100)
    jumlah_dana_dalam_negeri = models.DecimalField(max_digits=12,decimal_places=2,null=True, blank=True)
    jumlah_dana_luar_negeri = models.DecimalField(max_digits=12,decimal_places=2,null=True, blank=True)
    program_studi = models.ForeignKey(Program_Studi)
    ketua = models.ForeignKey(Anggota, related_name='ketua')
    anggota = models.ManyToManyField(Anggota)
    status_data = models.CharField(max_length=100, choices=(
        ('Valid', 'Valid'),
        ('Tidak Valid', 'Tidak Valid'),
        ('Belum diverifikasi', 'Belum diverifikasi')
    ))
    penginput = models.ForeignKey(User, blank=True, null=True)
    file_path = models.FileField(upload_to="Upload", validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    date = models.DateField(auto_now_add=True, blank=True)
    flag = models.CharField(max_length=100, choices=(
        ('Draft', 'Draft'),
        ('Publish', 'Publish')
    ))

    def __unicode__(self):
        return self.judul_penelitian
    class Meta:
        verbose_name_plural = 'Penelitian'

# class importPenelitian(CsvModel):
#     class Meta:
#         dbModel = Penelitian
#         delimeter = ";"

class Penelitian_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role)
    authors = models.ForeignKey(Authors,to_field='authors')
    judul_penelitian = models.ForeignKey(Penelitian,related_name='+',default='judul')

    def __unicode__(self):
        return self.authors_id

class History_Import(models.Model):
    class Meta:
        verbose_name_plural = 'History'

    log_import = models.CharField(max_length=500)
    username = models.CharField(max_length=200)
    upload = models.FileField(upload_to="Import", validators=[FileExtensionValidator(allowed_extensions=['xls'])])
    tanggal = models.DateField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.upload

class Log(models.Model):
    class Meta:
        verbose_name_plural = 'Logging'

    nama = models.CharField(max_length=200)
    tipe = models.CharField(max_length=200)
    aktivity = models.CharField(max_length=500)
    waktu = models.DateField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.waktu




# class Kegiatan(models.Model):
#     class Meta:
#         verbose_name_plural = 'Kegiatan'
#
#     kegiatan = models.CharField(max_length=500)
#
#     def __unicode__(self):
#         return self.kegiatan
