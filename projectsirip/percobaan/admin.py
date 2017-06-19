# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Authors)
admin.site.register(Role)
admin.site.register(Fokus_Penelitian)
admin.site.register(Fakultas)
admin.site.register(Program_Studi)
admin.site.register(pemerintah)
admin.site.register(Asal_Sumber_Dana)
admin.site.register(User)
admin.site.register(Jenis_Penelitian)
admin.site.register(Penelitian)
admin.site.register(Penelitian_Authors_Role)