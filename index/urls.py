#-_- coding: utf-8 -_-
from django.conf.urls import patterns, include, url
from index import views
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    url(r'^login/$', login, name='index'),
    #url(r'^login/$', views.login, name='login'),
    #url(r'^regist/$', views.regist, name='regist'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^index/$', views.index, name='index'),
)

