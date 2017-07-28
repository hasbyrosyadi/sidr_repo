# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals

import datetime
import requests
import xlrd
from data_importer.importers import XLSImporter
from django import forms
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.conf import settings
from .models import *


def crud_log(request, tipe, aktivitas):
    model = Log()
    model.nama = request.user.username
    model.tipe = tipe
    model.aktivity = aktivitas
    model.save()

def export_xls(request):
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='application/ms-excel;charset=utf-8')
    response['Content-Disposition'] = 'attachment; filename=hibah-penelitian.xls'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8'))

    daftarpenelitian = Penelitian.objects.all()

    writer.writerow([
        smart_str(u"Judul Penelitian"),
        smart_str(u"Nomor Kontrak"),
        smart_str(u"Tahun Pelaksanaan"),
        smart_str(u"Jenis Penelitian"),
        smart_str(u"Bidang Penelitian"),
        smart_str(u"Asal Sumber Dana"),
        smart_str(u"Jenis Sumber Dana"),
        smart_str(u"Nama Sumber Dana"),
        smart_str(u"Ketua"),
        smart_str(u"Anggota"),
        smart_str(u"Jumlah Dana Dalam Negeri"),
        smart_str(u"Jumlah Dana Luar Negeri"),
        smart_str(u"Status Data"),
        smart_str(u"Program studi"),
        smart_str(u"Penginput"),
        smart_str(u"Flag")
    ])
    for obj in daftarpenelitian:
        asalSumberDana = []
        for sumberDana in obj.asal_sumber_dana.all():
            asalSumberDana.append(sumberDana.sumber_dana)
        seluruhAnggota = []
        for gota in obj.anggota.all():
            seluruhAnggota.append(gota.nama)

        writer.writerow([
            smart_str(obj.judul_penelitian),
            smart_str(obj.nomor_kontrak),
            smart_str(obj.tahun_pelaksanaan),
            smart_str(obj.jenis_penelitian),
            smart_str(obj.bidang_penelitian),
            smart_str(', '.join(asalSumberDana)),
            smart_str(obj.jenis_sumber_dana),
            smart_str(obj.nama_sumber_dana),
            smart_str(obj.ketua),
            smart_str(', '.join(seluruhAnggota)),
            smart_str(obj.jumlah_dana_dalam_negeri),
            smart_str(obj.jumlah_dana_luar_negeri),
            smart_str(obj.get_status_data_display()),
            smart_str(obj.program_studi),
            smart_str(obj.penginput),
            smart_str(obj.get_flag_display())
        ])
    return response

def get_nama(request):
    akun = ('sirip', '5irip2017')
    response = requests.get("https://api.cs.ui.ac.id/sifasilkom/sipeg/staffs/", auth=akun)
    data = response.json()
    for hasil in data:
        test = Anggota()
        test.nama = hasil['nama_staf']
        test.nip = hasil['nip']
        test.username = hasil['username']
        test.save()

class hasilUpload(CreateView):
    template_name = 'Import.html'
    model = History_Import
    def get_success_url(self):
        return '/percobaan/listpenelitian/'

    fields = ['upload']

    def form_valid(self, form):
        object = form.save(commit=True)
        object.save()
        filepath = settings.MEDIA_ROOT+'/'+ object.upload.name
        importFile(filepath)
        return super(hasilUpload, self).form_valid(form)

def hapus(request):
    model = Penelitian.objects.all().delete()
    return redirect('/percobaan/listpenelitian/')

def importFile(filepath):
    import xlrd
    wb = xlrd.open_workbook(filename=filepath)
    sh1 = wb.sheet_by_index(0)
    data = []
    for rownum in range(sh1.nrows):
        data += [sh1.row_values(rownum)]

    data = data[1:]
    for line in data:
        # for d in range(0, 13):
        #     print 'line', d,'=', line[d], 'tipe = ', type(line[d])

        serial = line[2]
        sc = (serial - 25569) * 86400.0
        x = datetime.datetime.utcfromtimestamp(sc)

        JP = Jenis_Penelitian.objects.get(nama_jenis_penelitian=line[3])
        BP = Fokus_Penelitian.objects.get(nama=line[4])
        ketua = Anggota.objects.get(nama=line[7])
        JSD = Pemerintah.objects.get(instansi=line[9])
        PS = Program_Studi.objects.get(program_studi=line[12])
        anggota = []
        for d in Anggota.objects.all():
            anggota.append(
                d.nama
            )

        NamaAnggota = (', '.join(anggota))
        pisah = line[8].split(', ')
        print pisah, 'tipe = ',type(pisah)

        if (NamaAnggota.__contains__(line[8])):
            print 'masuk'
            nama = []
            for d in pisah:
                nama.append(
                    Anggota.objects.get(nama__contains=d)
                )
        else:
            return messages.error(request, 'data tidak tersedia')

        ASD = []
        if ('dalam negeri, luar negeri/asing' == line[5].lower()):
            ASD = Asal_Sumber_Dana.objects.all()
        elif('dalam negeri' == line[5].lower()):
            ASD = Asal_Sumber_Dana.objects.filter(sumber_dana__iexact=line[5])
        elif ('luar negeri/asing' == line[5].lower()):
            ASD = Asal_Sumber_Dana.objects.filter(sumber_dana__iexact=line[5])
        else:
            pass

        test = Penelitian()
        test.judul_penelitian = line[0]
        test.nomor_kontrak = line[1]
        test.tahun_pelaksanaan = x.date()
        test.jenis_penelitian = JP
        test.bidang_penelitian = BP
        # test.asal_sumber_dana = ASD
        test.nama_sumber_dana = line[6]
        test.ketua = ketua
        # test.anggota = line[8]
        test.jenis_sumber_dana = JSD
        test.jumlah_dana_dalam_negeri = line[10]
        test.jumlah_dana_luar_negeri = line[11]
        test.program_studi = PS
        test.save()

    for sumberdana in ASD:
        # print "ASD = ", sumberdana, "- tipe = ", type(sumberdana)
        test.asal_sumber_dana.add(sumberdana)
    for seluruhAngota in nama:
        # print "coba = ", seluruhAngota, "- tipe = ", type(seluruhAngota)
        test.anggota.add(seluruhAngota)




class createPenelitian(CreateView):
    template_name = 'create_form_penelitian.html'
    model = Penelitian
    def get_success_url(self):
        return '/percobaan/'+ str(self.object.id)

    fields = ['judul_penelitian', 'nomor_kontrak', 'tahun_pelaksanaan', 'jenis_penelitian', 'bidang_penelitian'
              ,'asal_sumber_dana', 'jenis_sumber_dana', 'nama_sumber_dana', 'ketua', 'anggota', 'jumlah_dana_dalam_negeri', 'jumlah_dana_luar_negeri',
              'status_data', 'program_studi', 'penginput', 'file_path', 'flag']

    def get_context_data(self, **kwargs):
        context = super(createPenelitian, self).get_context_data(**kwargs)
        context['fakultas'] = Fakultas.objects.all()
        context['fokus_penelitian'] = Fokus_Penelitian.objects.all()
        return context

    def get_form(self, form_class=None):
        form = super(createPenelitian, self).get_form(form_class=None)
        form.fields["asal_sumber_dana"].widget = forms.CheckboxSelectMultiple()
        form.fields["nomor_kontrak"] = MultiExampleField()
        form.fields["tahun_pelaksanaan"].widget = forms.SelectDateWidget(attrs={'style':'display: inline-block; margin-left: 0px; width: 200px'}, years=range(1990, 2030))
        return form

class MultiWidgetBasic(forms.widgets.MultiWidget):
    def __init__(self, attrs=None):
        widgets = [forms.TextInput(attrs={'style':'display: inline-block; margin-left: 0px; width: 160px'}),
                   forms.TextInput(attrs={'style':'display: inline-block; margin-left: 18px; width: 160px'}),
                   forms.TextInput(attrs={'style':'display: inline-block; margin-left: 18px; width: 160px'}),
                   forms.TextInput(attrs={'style':'display: inline-block; margin-left: 17px; width: 160px'})]
        super(MultiWidgetBasic, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return value
        else:
            return ['','','','']

class MultiExampleField(forms.fields.MultiValueField):
    widget = MultiWidgetBasic

    def __init__(self, *args, **kwargs):
        list_fields = [forms.fields.CharField(max_length=31),
                       forms.fields.CharField(max_length=31),
                       forms.fields.CharField(max_length=31),
                       forms.fields.CharField(max_length=31)]
        super(MultiExampleField, self).__init__(list_fields, *args, **kwargs)

    def compress(self, values):
        if values:
            values = "/".join(values)
        return values

class deletePenelitian(DeleteView):
    template_name = 'delete_form_penelitian.html'
    model = Penelitian
    def get_success_url(self):
        return '/percobaan/listpenelitian/'

    fields = ['judul_penelitian', 'nomor_kontrak', 'tahun_pelaksanaan', 'jenis_penelitian', 'bidang_penelitian',
              'asal_sumber_dana', 'jenis_sumber_dana', 'nama_sumber_dana', 'ketua', 'anggota',
              'jumlah_dana_dalam_negeri', 'jumlah_dana_luar_negeri', 'status_data', 'program_studi', 'penginput', 'file_path', 'flag']

class updatePenelitian(UpdateView):
    template_name = 'update_form_penelitian.html'
    model = Penelitian
    def get_success_url(self):
        return '/percobaan/'+ str(self.object.id)

    fields = ['judul_penelitian', 'nomor_kontrak', 'tahun_pelaksanaan', 'jenis_penelitian', 'bidang_penelitian', 'asal_sumber_dana',
              'jenis_sumber_dana', 'nama_sumber_dana', 'ketua', 'anggota', 'jumlah_dana_dalam_negeri', 'jumlah_dana_luar_negeri',
              'status_data', 'program_studi', 'penginput', 'file_path', 'flag']

    def form_valid(self, form):
        nama = self.request
        crud_log(nama, 'update', form.cleaned_data['judul_penelitian'])
        return super(updatePenelitian, self).form_valid(form)

    # def dispatch(self, request, *args, **kwargs):
    #     form = self.get_form()
    #     if form.is_valid():
    #         crud_log(request, 'update', form.cleaned_data['judul_penelitian'])
    #         messages.success(request, 'Data berhasil diperbaharui')
    #         form.save()
    #         return redirect('/percobaan/listpenelitian/')
    #     else:
    #         messages.error(request, 'data gagal update')
    #         print form.errors
    #         return self.form_invalid(form)

    def get_context_data(self):
        context = super(updatePenelitian, self).get_context_data()
        context['fakultas'] = Fakultas.objects.all()
        context['fokus_penelitian'] = Fokus_Penelitian.objects.all()
        return context

    def get_form(self, form_class=None):
        form = super(updatePenelitian, self).get_form(form_class=None)
        form.fields["asal_sumber_dana"].widget = forms.CheckboxSelectMultiple()
        form.fields["tahun_pelaksanaan"].widget = forms.SelectDateWidget(attrs={'style':'display: inline-block; margin-left: 0px; width: 200px'}, years=range(1990, 2030))
        return form

class listpenelitian(ListView):
    template_name = 'List_Hibah_Penelitian.html'
    model = Penelitian
    context_object_name = "DaftarPenelitian"

class formPesan(SuccessMessageMixin, ListView):
    template_name = 'success.html'
    list = Penelitian.objects.all()
    for data in list:
        if (data == True):
            success_message = data.judul_penelitian, ' data berhasil disimpan'
        else:
            success_message = data.judul_penelitian, ' data tidak berhasil disimpan'

class detailPenelitian(DetailView):
    template_name = 'review.html'
    model = Penelitian

def penelitian(request, penelitian_id):
    return render(request, 'review.html', {
        'penelitian':get_object_or_404(Penelitian, id=penelitian_id)
    })

def index(request):
    all_penelitian = Penelitian.objects.all()
    html = ''
    for penelitian in all_penelitian:
        url = "/percobaan/" + str(penelitian.id) + "/"
        html += '<a href="' + url + '">' + penelitian.judul_penelitian + '</a><br>'
    return HttpResponse(html)
