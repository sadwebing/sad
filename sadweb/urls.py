from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sadweb.views.home', name='home'),
    # url(r'^sadweb/', include('sadweb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'index.views.index', name='index'),
    #url(r'^$', include('index.urls')),
    url(r'^accounts/', include('index.urls')),
    url(r'^deploy/', include('saltstack.urls')),
    url(r'^index/', include('index.urls')),
    url(r'^keys/', include('managekeys.urls')),
    #url(r'^(\d{1,2})/$', include('index.urls')),
    url(r'^(\d{1,2})/$', 'index.views.TimeAfter', name='TimeAfter'),
    url(r'^admin/', include(admin.site.urls)),
)
