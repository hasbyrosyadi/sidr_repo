from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('judul','kontrak_penelitian','tahun','jenis_penelitian','bidang_penelitian','tujuan_sosial_ekonomi','asal_sumber_dana','jenis_sumber_dana','institusi_sumber_dana','jumlah_dana','departemen','program_studi','pusat_riset','status_data','path_berkas_pendukung')
    def clean_judul(self)
        judul = self.cleaned_data.get('judul')
        if email == ""
            raise forms.ValidationError("Judul tidak boleh kosong")
        return judul
    def clean_kontrak_penelitian(self)
        kontrak_penelitian = self.cleaned_data.get('kontrak_penelitian')
        return kontrak_penelitian
    def clean_tahun(self)
        tahun = self.cleaned_data.get('tahun')
        return tahun
    def clean_jenis_penelitian(self)
        jenis_penelitian= self.cleaned_data.get('jenis_penelitian')
        return jenis_penelitian
    def clean_bidang_penelitian(self)
        bidang_penelitian = self.cleaned_data.get('bidang_penelitian')
        return bidang_penelitian
    def clean_tujuan_sosial_ekonomi(self)
        tujuan_sosial_ekonomi = self.cleaned_data.get('tujuan_sosial_ekonomi')
        return tujuan_sosial_ekonomi
    def clean_asal_sumber_dana(self)
        asal_sumber_dana = self.cleaned_data.get('asal_sumber_dana')
        return asal_sumber_dana
    def clean_jenis_sumber_dana(self)
        jenis_sumber_dana = self.cleaned_data.get('jenis_sumber_dana')
        return jenis_sumber_dana
    def clean_institusi_sumber_dana(self)
        institusi_sumber_dana = self.cleaned_data.get('institusi_sumber_dana')
        return institusi_sumber_dana
    def clean_jumlah_dana(self)
        jumlah_dana= self.cleaned_data.get('jumlah_dana')
        return jumlah_dana
    def clean_departemen(self)
        departemen = self.cleaned_data.get('departemen')
        return departemen
    def clean_program_studi(self)
        program_studi = self.cleaned_data.get('program_studi')
        return program_studi
    def clean_pusat_riset(self)
        pusat_riset = self.cleaned_data.get('pusat_riset')
        return pusat_riset
    def clean_path_berkas_pendukung(self)
        path_berkas_pendukung = self.cleaned_data.get('path_berkas_pendukung')
        return path_berkas_pendukung