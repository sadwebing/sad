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







#form list
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=100)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())

#regist
def regist(req):
    if req.method =='POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #get the form data
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            User.objects.create(username=username, password=password)
            return HttpResponse('注册成功！')
    else:
        uf = UserForm()
    return render_to_response('regist.html', {'uf': uf}, context_instance=RequestContext(req))

#login
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #get the form data
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #compare data to the database
            result = User.objects.filter(username__exact=username, password=password)
            if result:
                #user and password correct, then redirect to index
                response = HttpResponseRedirect('/index/index/')
                #add user to browser cookie, valid time is 600
                response.set_cookie('username', username, 600)
                return response
            else:
                #user or password wrong
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html', {'uf': uf}, context_instance=RequestContext(req))

##login successful
#def index(req):
#    username = req.COOKIES.get('username', '')
#    return render_to_response('index.html', {'username': username})

#logout
def logout(req):
    response = HttpResponse('退出！')
    #clear the username in cookie
    response.delete_cookie('username')
    return response


###test###
def Hello(request):
    return HttpResponse('Hello World!')

def CurrentTime(request):
    CurrentTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    Content = "<html><body>Current time is %s.<body/><html/>" %CurrentTime
    return HttpResponse(Content)

def TimeAfter(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    CurrentTime = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    TimeAfter = (datetime.now() + timedelta(hours=offset)).strftime('%Y/%m/%d %H:%M:%S')
    #assert False
    TimeDic = {'CurrentTime': CurrentTime, 'offset': offset, 'TimeAfter': TimeAfter }
    t = get_template('index.html')
    Html = t.render(Context(TimeDic))
    #Content = "<html><body>Current time is %s, in %s hours, time is %s.<body/><html/>" %(CurrentTime, offset, TimeAfter)
    return HttpResponse(Html)

