# -*- coding: utf-8 -*-
# Create your views here.
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from .models import *

class addPenelitian(CreateView):
    template_name = 'create_form_penelitian.html'
    model = Penelitian
    def get_success_url(self):
        return '/percobaan/'+ str(self.object.id)
    fields = ['judul_penelitian', 'nomor_kontrak', 'tahun_pelaksanaan', 'jenis_penelitian', 'bidang_penelitian'
              ,'asal_sumber_dana', 'jenis_sumber_dana', 'nama_sumber_dana', 'jumlah_dana_dalam_negeri', 'jumlah_dana_luar_negeri',
              'status_data', 'program_studi', 'penginput', 'file_path', 'flag']

class deletePenelitian(DeleteView):
    template_name = 'delete_form_penelitian.html'
    model = Penelitian
    def get_success_url(self):
        return '/percobaan/'

    fields = ['judul_penelitian', 'nomor_kontrak', 'tahun_pelaksanaan', 'jenis_penelitian', 'bidang_penelitian', 'asal_sumber_dana', 'jenis_sumber_dana', 'nama_sumber_dana', 'jumlah_dana_dalam_negeri',
              'jumlah_dana_luar_negeri',
              'status_data', 'program_studi', 'penginput', 'file_path', 'flag']

class updatePenelitian(UpdateView):
    template_name = 'update_form_penelitian.html'
    model = Penelitian
    def get_success_url(self):
        return '/percobaan/successupdate/' + str(self.object.id)

    fields = ['judul_penelitian', 'nomor_kontrak', 'tahun_pelaksanaan', 'jenis_penelitian', 'bidang_penelitian', 'asal_sumber_dana', 'jenis_sumber_dana', 'nama_sumber_dana', 'jumlah_dana_dalam_negeri',
              'jumlah_dana_luar_negeri',
              'status_data', 'program_studi', 'penginput', 'file_path', 'flag']

    def get_form(self, form_class=None):
        form = super(updatePenelitian, self).get_form(form_class)
        form.helper = FormHelper()
        form.helper.form_class = "form-horizontal"
        form.helper.label_class = "col-lg-3"
        form.helper.field_class = "col-lg-2"
        form.helper.add_input(Submit('submit', 'simpan'))
        return form

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

