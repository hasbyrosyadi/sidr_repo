# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def penelitian(request, penelitian_id):
    all_penelitian = Penelitian.objects.all()
    html = ''
    for penelitian in all_penelitian:
        url = "/percobaan/penelitian"


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

