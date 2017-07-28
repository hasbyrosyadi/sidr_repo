"""projectsirip URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^(?P<penelitian_id>[0-9]+)/$', login_required(views.penelitian), name='penelitian'),
    url(r'^createpenelitian/$', login_required(views.createPenelitian.as_view()), name='createPenelitian'),
    url(r'^updatepenelitian/(?P<pk>[0-9]+)/$', login_required(views.updatePenelitian.as_view()), name='updatePenelitian'),
    url(r'^deletepenelitian/(?P<pk>[0-9]+)/$', login_required(views.deletePenelitian.as_view()), name='deletePenelitian'),
    url(r'^listpenelitian/$', login_required(views.listpenelitian.as_view()), name='listPenelitian'),
    url(r'^detailpenelitian/(?P<pk>[0-9]+)/$', login_required(views.detailPenelitian.as_view()), name='detailPenelitian'),
    url(r'^download/$', views.export_xls, name='download'),
    url(r'^respon/$', views.get_nama, name='respon'),
    url(r'^import/$', login_required(views.hasilUpload.as_view()), name='import'),
    url(r'^json/$', views.importFile, name='import'),
    url(r'^sukses/$', login_required(views.formPesan.as_view), name='success')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)