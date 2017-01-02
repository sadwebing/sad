# -*- coding: utf-8 -*-
from django.db import models

class Domain(models.Model):
    """
    用于存储域名，解析
    """
    product = models.CharField(max_length=50, unique=False, verbose_name=u'所属产品')
    abbr = models.CharField(max_length=20, unique=True, verbose_name=u'简称')
    domain = models.CharField(max_length=50, unique=False, verbose_name=u'域名')
    record = models.CharField(max_length=20, verbose_name=u'解析记录')

    def __unicode__(self):
        return u'{0} {1} {2} {3}'.format(self.product, self.abbr, self.domain, self.record)
    #**class Meta:**
    #    **ordering = ['product', 'abbr']**
