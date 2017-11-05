"""pytx URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.decorators.csrf import csrf_exempt

from djzen.urls import zen_url

import pytx.views
import conference.views

from graphene_django.views import GraphQLView

urlpatterns = [
    zen_url('2015/', pytx.views.archive),
    zen_url('2014/', pytx.views.archive),
    zen_url('2013/', pytx.views.archive),
    zen_url('release-stream', pytx.views.release_stream),
    
    zen_url('admin/', admin.site.urls),
    zen_url('data-graph', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    zen_url('favicon.ico', conference.views.favicon),
    zen_url('service-worker.js', conference.views.sw),
    zen_url('release', conference.views.release),
    zen_url('manifest.json', conference.views.manifest),
    zen_url('browserconfig.xml', conference.views.browserconfig),
    zen_url('conference/', include('conference.event.urls')),
    zen_url('.*', conference.views.frontend),
]
