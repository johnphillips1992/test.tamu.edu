from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin




admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('tamu.coa.settings.general.urls')),
    url('^accounts/logout/$', 'django.contrib.auth.views.logout',
        kwargs={'template_name': 'accounts/logged_out.html'}),
    url('^accounts/login/$', 'django.contrib.auth.views.login',
        kwargs={'template_name': 'accounts/login.html'}),
    url(r'^news/', include('newsy.urls')),
)
