from django.conf.urls import patterns, include, url

from django.contrib import admin
import djangoblog

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^djangoblog/create', 'djangoblog.views.create'),
    url(r'^djangoblog/update','djangoblog.views.update')
)
