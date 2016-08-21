#-_- coding:utf-8 -_-
from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'managekeys.views',
    url(r'^show/$', 'manageMinionKeys', name='keys_show'),
    url(r'^api/$', 'manageMinionKeysAPI', name='keys_api'),
    url(r'^(?P<action>accept|delete|reject)/$', 'actionMinionKeys', name='action_keys'),
)

