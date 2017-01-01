#-_- coding: utf-8 -_-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.template import Context, RequestContext
from django import forms
from datetime import datetime, timedelta
#from models import User
from django.contrib.auth.models import User
from django.contrib import auth
from index.models import ServStatus, ProcStatus, MiniKeys

@login_required
def index(request):
    #return HttpResponse('success!')
    '''
    index page
    '''

    ret = {}

    try:
        server_status = ServStatus.objects.order_by('-id')[0]
        # SELECT * from `servstatus` order by id DESC limit 1

        ret['nowtime'] = server_status.nowtime
        print ret['nowtime']
        ret['sysone'] = server_status.sysone
        ret['sysfive'] = server_status.sysfive
        ret['sysfifteen'] = server_status.sysfifteen
        ret['cpuperc'] = server_status.cpuperc
        ret['memtotal'] = server_status.memtotal
        ret['memused'] = server_status.memused
        ret['memperc'] = server_status.memperc
        ret['disktotal'] = server_status.disktotal
        ret['diskused'] = server_status.diskused
        ret['diskperc'] = server_status.diskperc

    # except OperationalError,e:
    except Exception, e:
        # ret['serv_error_code'] = e[0]
        # ret['serv_error_content'] = e[1]
        ret['nowtime'] = 'Null'
        ret['sysone'] = 'Null'
        ret['sysfive'] = 'Null'
        ret['sysfifteen'] = 'Null'
        ret['cpuperc'] = 'Null'
        ret['memtotal'] = 'Null'
        ret['memused'] = 'Null'
        ret['memperc'] = 'Null'
        ret['disktotal'] = 'Null'
        ret['diskused'] = 'Null'
        ret['diskperc'] = 'Null'

    try:
        proc_status = ProcStatus.objects.order_by('-id')[0]
        # SELECT * from `procstatus` order by id DESC limit 1

        ret['proctime'] = proc_status.nowtime
        print ret['proctime']
        if proc_status.saltproc == 0:
            ret['saltst'] = '正常'
        elif proc_status.saltproc == 1:
            ret['saltst'] = '异常'
        else:
            ret['saltst'] = 'UNKNOWN'

        if proc_status.apiproc == 0:
            ret['apist'] = '正常'
        elif proc_status.apiproc == 1:
            ret['apist'] = '异常'
        else:
            ret['apist'] = 'UNKNOWN'

        if proc_status.myproc == 0:
            ret['myst'] = '正常'
        elif proc_status.myproc == 1:
            ret['myst'] = '异常'
        else:
            ret['myst'] = 'UNKNOWN'

        if proc_status.snmproc == 0:
            ret['snmpst'] = '正常'
        elif proc_status.snmproc == 1:
            ret['snmpst'] = '异常'
        else:
            ret['snmpst'] = 'UNKNOWN'

    # except OperationalError,e:
    except Exception, e:
        # ret['proc_error_code'] = e[0]
        # ret['proc_error_content'] = e[1]
        ret['saltst'] = 'Null'
        ret['apist'] = 'Null'
        ret['myst'] = 'Null'
        ret['snmpst'] = 'Null'

    try:
        minion_keys = MiniKeys.objects.order_by('-id')[0]
        # SELECT * from `minikeys` order by id DESC limit 1

        ret['mktime'] = minion_keys.nowtime
        print  ret['mktime']
        ret['num_miniall'] = minion_keys.miniall
        ret['num_miniup'] = minion_keys.minion
        ret['num_minidown'] = minion_keys.miniout
        ret['num_mini'] = minion_keys.keyall
        ret['num_minipre'] = minion_keys.keypre
        ret['num_minirej'] = minion_keys.keyrej

    # except OperationalError,e:
    except Exception, e:
        # ret['mini_error_code'] = e[0]
        # ret['mini_error_content'] = e[1]
        ret['mktime'] = 'Null'
        ret['num_miniall'] = 'Null'
        ret['num_miniup'] = 'Null'
        ret['num_minidown'] = 'Null'
        ret['num_mini'] = 'Null'
        ret['num_minipre'] = 'Null'
        ret['num_minirej'] = 'Null'

    streslut = ''
    #try:
    #    operate_rec = OperateRecord.objects.order_by('-id')[0:8]
    #    for result in operate_rec:
    #        streslut += '%s %s %s %s\n' % (result.nowtime, result.username, result.user_operate, result.simple_tgt)
    #except Exception, e:
    #    log.error("No data acquired.")

    return render(
        request,
        'index.html',
        {
            'ret': ret,
            'stret': streslut
        }
    )

def logout(request):
    response = HttpResponse('退出！')
    #clear the username in cookie
    #response.delete_cookie('username')
    #return response
    auth.logout(request)
    return HttpResponseRedirect('/')
