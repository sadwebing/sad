#-_- coding:utf-8 -_-
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'navigation.views',
    url(r'^list/$', 'list', name='navigation_list'),
)
