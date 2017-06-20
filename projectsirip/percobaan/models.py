    # -*- coding: utf-8  -*-

# Create your models here.
from django.db import models
from isbn_field import ISBNField

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
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)

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


class Makalah(models.Model):

    class Meta:
        verbose_name_plural = 'Makalah'
    judul_makalah = models.CharField(max_length=500)
    abstrak = models.TextField(max_length=9999)
    tingkat = (
        ('I', 'Internasional'),
        ('N', 'Nasional'),
    )
    tingkat_forum = models.CharField(max_length=1, choices=tingkat)
    tahun_pelaksanaan = models.PositiveSmallIntegerField()
    forum_penyelenggara = models.CharField(max_length=100)
    institusi_penyelenggara = models.CharField(max_length=100)
    tanggal_mulai = models.DateField(auto_now=True)
    tanggal_selesai = models.DateField(auto_now=True)
    tempat_pelaksanaan = models.CharField(max_length=100)
    status_pemakalahan =  models.CharField(max_length=100)
    link = models.URLField()
    nama_sumber_dana = models.CharField(max_length=100)
    pusat_riset = models.CharField(max_length=100)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    hibah_terkait = models.ForeignKey(Penelitian,related_name='+',default='judul')
    def __unicode__(self):
        return self.judul_makalah


class Makalah_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    judul_makalah = models.ForeignKey(Makalah,related_name='+',default='judul')

    def __unicode__(self):
        return self.authors_id

# kegiatan_forum_ilmiah.xls
class Forum_Ilmiah(models.Model):

    class Meta:
        verbose_name_plural = 'Forum'
    nama_kegiatan= models.CharField(max_length=500)
    abstrak = models.TextField(max_length=9999)
    tingkat = (
        ('I', 'Internasional'),
        ('N', 'Nasional'),
    )
    tingkat_forum = models.CharField(max_length=1, choices=tingkat)
    tahun_pelaksanaan = models.PositiveSmallIntegerField()
    penyelenggara = models.CharField(max_length=100)
    unit_penyelenggara = models.CharField(max_length=100)
    mitra_sponsor = models.CharField(max_length=100)
    tanggal_pelaksanaan = models.DateField(auto_now=True)
    tempat_pelaksanaan = models.CharField(max_length=100)
    link = models.URLField()
    nama_sumber_dana = models.CharField(max_length=100)
    pusat_riset = models.CharField(max_length=100)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    hibah_terkait = models.ForeignKey(Penelitian,related_name='+',default='judul')
    def __unicode__(self):
        return self.nama_kegiatan

class Forum_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    nama_kegiatan = models.ForeignKey(Forum_Ilmiah,related_name='+',default='forum')

    def __unicode__(self):
        return self.authors_id

# buku_teks_ajar.xls
class Buku_Teks_Ajar(models.Model):

    class Meta:
        verbose_name_plural = 'buku'
    judul_buku= models.CharField(max_length=500)
    tahun_terbit = models.PositiveSmallIntegerField()
    isbn = ISBNField()
    jumlah_halaman = models.PositiveSmallIntegerField()
    penerbit = models.CharField(max_length=100)
    pusat_riset = models.CharField(max_length=100)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    hibah_terkait = models.ForeignKey(Penelitian,related_name='+',default='judul')

    def __unicode__(self):
        return self.judul_buku

class Book_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    judul_buku = models.ForeignKey(Buku_Teks_Ajar,related_name='+',default='forum')

    def __unicode__(self):
        return self.authors_id


#publikasi_ilmiah_jurnal.xls
class Jurnal_Ilmiah(models.Model):

    class Meta:
        verbose_name_plural = 'Forum'
    judul_jurnal= models.CharField(max_length=500)
    nama_jurnal= models.CharField(max_length=500)
    abstrak = models.TextField(max_length=9999)
    tingkat = (
        ('I', 'Internasional'),
        ('N', 'Nasional'),
    )
    tingkat_jurnal = models.CharField(max_length=1, choices=tingkat)
    impact_factor =  models.FloatField(null=True, blank=True, default=None)
    issn = models.TextField(max_length=9)
    volume = models.PositiveSmallIntegerField()
    nomor = models.PositiveSmallIntegerField()
    page = models.CharField(max_length=500)
    issue = models.PositiveSmallIntegerField()
    link = models.URLField()
    pusat_riset = models.CharField(max_length=100)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    hibah_terkait = models.ForeignKey(Penelitian,related_name='+',default='judul')
    def __unicode__(self):
        return self.judul_jurnal

class Jurnal_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    judul_jurnal = models.ForeignKey(Jurnal_Ilmiah,related_name='+',default='forum')

    def __unicode__(self):
        return self.authors_id

# luaran_lain.xls
class Luaran_Lain(models.Model):

    class Meta:
        verbose_name_plural = 'luaran'
    judul_luaran= models.CharField(max_length=500)
    tahun_publikasi = models.PositiveSmallIntegerField()
    jenis_luaran = (
        ('P', 'Prototipe'),
        ('M', 'Model'),
        ('D', 'Desain'),
    )
    jenis = models.CharField(max_length=1, choices=jenis_luaran)
    deskripsi_singkat = models.CharField(max_length=300)
    penerbit = models.CharField(max_length=100)
    pusat_riset = models.CharField(max_length=100)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    hibah_terkait = models.ForeignKey(Penelitian,related_name='+',default='judul')

    def __unicode__(self):
        return self.nama_kegiatan

class Luaran_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    judul_luaran = models.ForeignKey(Luaran_Lain,related_name='+',default='luaran')

    def __unicode__(self):
        return self.authors_id

# hak_kekayaan_intelektual.xls
class Hak_Kekayaan_Intelektual(models.Model):

    class Meta:
        verbose_name_plural = 'luaran'
    judul_HKI= models.CharField(max_length=500)
    tahun_pengajuan = models.PositiveSmallIntegerField()
    jenis_HKI = (
        ('H', 'Hak Cipta'),
        ('M', 'Model'),
        ('D', 'Desain'),
    )
    jenis = models.CharField(max_length=1, choices=jenis_HKI)
    status_HKI = (
        ('T', 'Terdaftar'),
        ('G', 'Granted'),
    )
    status = models.CharField(max_length=1, choices=status_HKI)
    nomor_pendaftaran = models.CharField(max_length=20)
    nomor_hki = models.PositiveSmallIntegerField()
    pusat_riset = models.CharField(max_length=100)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    hibah_terkait = models.ForeignKey(Penelitian,related_name='+',default='judul')

    def __unicode__(self):
        return self.nama_kegiatan

class HKI_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    judul_HKI = models.ForeignKey(Hak_Kekayaan_Intelektual,related_name='+',default='HKI')

    def __unicode__(self):
        return self.authors_id

#hibah_non_penelitian_kontrak_kerja.xls
class Hibah_Non_Penelitian_Kontrak_Kerja(models.Model):

    class Meta:
        verbose_name_plural = 'hibah_non_penelitian'
    nama_kegiatan= models.CharField(max_length=500)
    nomor_kontrak= models.CharField(max_length=500)
    tahun_penelitian = models.PositiveSmallIntegerField()
    jenis_kegiatan = (
        ('L', 'lain-lain'),
        ('P', 'penulisan buku'),
    )
    jenis = models.CharField(max_length=1, choices=jenis_kegiatan)
    tanggal_mulai = models.DateField(auto_now=True)
    tanggal_selesai = models.DateField(auto_now=True)
    unit_penyelenggara = models.CharField(max_length=100)
    nilai_kontrak_penghibahan =  models.FloatField(null=True, blank=True, default=None)
    sumber_dana= models.CharField(max_length=100)
    pusat_riset = models.CharField(max_length=100)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    hibah_terkait = models.ForeignKey(Penelitian,related_name='+',default='judul')

    def __unicode__(self):
        return self.nama_kegiatan

class Hibah_Non_Penelitian_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    nama_kegiatan = models.ForeignKey(Hibah_Non_Penelitian_Kontrak_Kerja,related_name='+',default='hibah_non_penelitian')

    def __unicode__(self):
        return self.authors_id

class Hibah_Non_Penelitian_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    judul_buku= models.CharField(max_length=300)
    penerbit= models.CharField(max_length=100)
    isbn = ISBNField()
    nama_kegiatan = models.ForeignKey(Hibah_Non_Penelitian_Kontrak_Kerja,related_name='+',default='hibah_non_penelitian')

    def __unicode__(self):
        return self.authors_id

#hibah_pengmas.xls
class hibah_Pengmas(models.Model):

    class Meta:
        verbose_name_plural = 'hibah_non_penelitian'
    nama_kegiatan= models.CharField(max_length=500)
    mitra_institusi = models.CharField(max_length=100)
    nomor_kontrak= models.CharField(max_length=500)
    tahun_penelitian = models.PositiveSmallIntegerField()
    jumlah_dosen = models.PositiveSmallIntegerField()
    jumlah_mahasiswa = models.PositiveSmallIntegerField()
    tahun_pelaksanaan = models.PositiveSmallIntegerField()
    lokasi_kegiatan = models.CharField(max_length=100)
    nilai_kontrak_penghibahan =  models.FloatField(null=True, blank=True, default=None)
    sumber_dana= models.CharField(max_length=100)
    pusat_riset = models.CharField(max_length=100)
    program_studi = models.ForeignKey(Program_Studi, on_delete=models.CASCADE)
    status_data = models.CharField(max_length=100)
    penginput = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=300)
    date = models.DateField(auto_now=True)
    hibah_terkait = models.ForeignKey(Penelitian,related_name='+',default='judul')

    def __unicode__(self):
        return self.nama_kegiatan

class Hibah_Pengmas_Authors_Role(models.Model):

    class Meta:
        verbose_name_plural = 'Author Role'
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    authors = models.ForeignKey(Authors,to_field='authors')
    nama_kegiatan = models.ForeignKey(hibah_Pengmas,related_name='+',default='hibah_pengmas')

    def __unicode__(self):
        return self.authors_id
