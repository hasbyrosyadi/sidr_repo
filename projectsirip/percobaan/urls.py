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
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<penelitian_id>[0-9]+)/$', views.penelitian, name='penelitian'),
    url(r'^addpenelitian/$', views.addPenelitian.as_view(), name='addPenelitian'),
    url(r'^updatepenelitian/(?P<pk>[0-9]+)/$', views.updatePenelitian.as_view(), name='updatePenelitian'),
    url(r'^deletepenelitian/(?P<pk>[0-9]+)/$', views.deletePenelitian.as_view(), name='deletePenelitian')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)