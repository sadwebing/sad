#!/usr/bin/python
#-_- coding: utf-8 -_-
#Created By Arno on 20170101
#Introduction: 用于同步域名列表

import sys,os
sys.path.append('/usr/local/sadweb')
from sadweb import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sadweb.settings")
from navigation.models import Domain

RootPath = '/usr/local/sadweb'
DomainTxt = RootPath + '/static/config/domain.txt'
RecordDic = {}
DomainList = []

with open(DomainTxt, u'r') as f:
    DomainListTmp = f.readlines()

#print DomainListTmp

def recorddic_db(RecordDic):
    try:
        D = Domain.objects.get(abbr=RecordDic['abbr'])
        D.abbr = RecordDic['abbr']
        D.product = RecordDic['product']
        D.domain = RecordDic['domain']
        D.record = RecordDic['record']
        D.save()
        #print " ".join(str(RecordDic) + "updated")
    except:
        D = Domain(product=RecordDic['product'], abbr=RecordDic['abbr'], domain=RecordDic['domain'], record=RecordDic['record'])
        D.save()
        #print u" ".join(str(RecordDic) + "inserted")

for Record in DomainListTmp:
    '''
    获取域名列表
    '''
    if '#' not in Record and Record != '':
        RecordDic['product'] = Record.replace('\n', '').split('|')[0]
        RecordDic['abbr'] = Record.replace('\n', '').split('|')[1]
        RecordDic['domain'] = Record.replace('\n', '').split('|')[2]
        RecordDic['record'] = Record.replace('\n', '').split('|')[3]
        recorddic_db(RecordDic)
        #print RecordDic
        #DomainList.append(RecordDic)
        #print DomainList













