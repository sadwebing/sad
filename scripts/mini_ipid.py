#!/usr/bin/python
# -*- coding: utf-8 -*-
# Guibin created on 2015/10/26
# version: 0.01

#from django.conf import settings
#settings.configure()
import sys,MySQLdb,urllib,salt,json
from salt.client import LocalClient
sys.path.append('/usr/local/sadweb')
from sadweb import settings
from saltstack.saltapi import SaltAPI
from sys import exit

class scriptApi(SaltAPI):
    def mini_grains(self, minionid):
        params = {'client':'local','tgt':minionid, 'fun':'grains.items'}
        #params = {}
        obj = urllib.urlencode(params)
        content = self.postRequest(obj)
        #content = self.postRequest(obj, prefix='/minions/WTT_100_56')
        return content
#print scriptApi(url=settings.SALT_API['url'],username=settings.SALT_API['user'],password=settings.SALT_API['password']).mini_grains()['return'][0]['WTT_100_56']['ipv4'][1]

#print settings.DATABASES['default']['HOST']

sapi = SaltAPI(
    url=settings.SALT_API['url'],
    username=settings.SALT_API['user'],
    password=settings.SALT_API['password']
    )

minionsup, minionsdown= sapi.mini_status()
minionsall = minionsup + minionsdown
conn = MySQLdb.connect(
    host = settings.DATABASES['default']['HOST'],
    user = settings.DATABASES['default']['USER'],
    passwd = settings.DATABASES['default']['PASSWORD'],
    db = settings.DATABASES['default']['NAME'],
    port = int(settings.DATABASES['default']['PORT']),
    charset='utf8',
)

cursor = conn.cursor()
ExeSqlSelect = '''SELECT * from `hostlist_idip`;'''
cursor.execute(ExeSqlSelect)
results = cursor.fetchall()
serv_list = {}
for row in results:
    minionid = row[1]
    minionip = row[2]
    serv_list[minionid] = minionip
ExeSqlInset = '''INSERT INTO `hostlist_idip`
        (`minionid`, `minionip`)
        VALUES
        (%s, %s)'''


for i in serv_list.keys():
    if i not in minionsall:
        ExeSqlDelete = '''DELETE FROM `hostlist_idip`
            WHERE `minionid`="%s"''' %i
        cursor.execute(ExeSqlDelete)
        conn.commit()

for minionid in minionsdown:
    if minionid in serv_list.keys():
        minionip = serv_list[minionid]
        if minionip != 'minionIsDown':
            minionip = 'minionIsDown'
            ExeSqlUpdate = '''UPDATE `hostlist_idip` SET
                `minionip`="%s" WHERE `minionid`="%s"''' %(minionip, minionid)
            conn.cursor().execute(ExeSqlUpdate)
            conn.commit()
    else:
        minionip = 'minionIsDown'
        conn.cursor().execute(ExeSqlInset,(minionid, minionip))
        conn.commit()
    #if minionid in serv_list.keys():
    #   print "%s is in database; MinionIp is %s" %(minionid, serv_list[minionid])

for minionid in minionsup:
    try:
        Ipv4 = sapi.mini_grains(minionid)['return'][0][minionid]['ipv4']
    except KeyError:
        Ipv4 = ''
    #print Ipv4
    if minionid in serv_list.keys():
        if '_' in minionid:
            for i in Ipv4:
                if i.split('.')[-1] == minionid.split('_')[-1]:
                    print i.split('.')[-1] + ' == ' + minionid.split('_')[-1]
                    minionip = i
                    break
                else:
                    print i.split('.')[-1] + ' != ' + minionid.split('_')[-1]
                    continue
            else:
                minionip = 'null'
        else:
            if len(Ipv4) > 2 and Ipv4[-1] == '127.0.0.1':
                minionip = Ipv4[0]
            elif len(Ipv4) > 2 and Ipv4[-1] != '127.0.0.1':
                minionip = Ipv4[-1]
            elif len(Ipv4) == 2 and Ipv4[1] != '127.0.0.1':
                minionip = Ipv4[1]
            else:
                minionip = Ipv4[0]
        print minionip, minionid
        ExeSqlUpdate = '''UPDATE `hostlist_idip` SET
                `minionip`="%s" WHERE `minionid`="%s"''' %(minionip, minionid)
        conn.cursor().execute(ExeSqlUpdate)
        conn.commit()
    else:
        if '_' in minionid:
            for i in Ipv4:
                if i.split('.')[-1] == minionid.split('_')[-1]:
                    minionip = i
                    break
                else:
                    continue
            else:
                minionip = 'null'
        else:
            if len(Ipv4) > 2 and Ipv4[-1] == '127.0.0.1':
                minionip = Ipv4[0]
            elif len(Ipv4) > 2 and Ipv4[-1] != '127.0.0.1':
                minionip = Ipv4[-1]
            elif len(Ipv4) == 2 and Ipv4[1] != '127.0.0.1':
                minionip = Ipv4[1]
            else:
                minionip = Ipv4[0]
        print minionip, minionid
        conn.cursor().execute(ExeSqlInset,(minionid, minionip))
        conn.commit()

