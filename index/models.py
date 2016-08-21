from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class ServStatus(models.Model):
    nowtime = models.DateTimeField(blank=True, null=True)
    sysone = models.CharField(max_length=10, blank=True)
    sysfive = models.CharField(max_length=10, blank=True)
    sysfifteen = models.CharField(max_length=10, blank=True)
    cpuperc = models.CharField(max_length=10, blank=True)
    memtotal = models.CharField(max_length=10, blank=True)
    memused = models.CharField(max_length=10, blank=True)
    memperc = models.CharField(max_length=10, blank=True)
    disktotal = models.CharField(max_length=10, blank=True)
    diskused = models.CharField(max_length=10, blank=True)
    diskperc = models.CharField(max_length=10, blank=True)
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s %s %s %s %s' %(
            self.nowtime, self.sysone, self.sysfive, self.sysfifteen, self.cpuperc, self.memtotal, self.memused,self.memperc, self.disktotal, self.diskused, self.diskperc)

class ProcStatus(models.Model):
    nowtime = models.DateTimeField(blank=True, null=True)
    saltproc = models.IntegerField(blank=True, null=True)
    apiproc = models.IntegerField(blank=True, null=True)
    myproc = models.IntegerField(blank=True, null=True)
    snmproc = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return u'%s %s %s %s %s' %(self.nowtime, self.saltproc, self.apiproc, self.myproc, self.snmproc)

class MiniKeys(models.Model):
    nowtime = models.DateTimeField(blank=True, null=True)
    miniall = models.IntegerField(blank=True, null=True)
    minion = models.IntegerField(blank=True, null=True)
    miniout = models.IntegerField(blank=True, null=True)
    keyall = models.IntegerField(blank=True, null=True)
    keypre = models.IntegerField(blank=True, null=True)
    keyrej = models.IntegerField(blank=True, null=True)
    def __unicode__(self):
        return u'%s %s %s %s %s %s %s' %(self.nowtime, self.miniall, self.minion, self.miniout, self.keyall, self.keypre, self.keyrej)
