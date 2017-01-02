#!/usr/bin/python
#-_- coding: utf-8 -_-
#Created By Arno on 20170101
#Introduction: 用于同步域名列表

from navigation.models import Domain
import sys
sys.path.append('D:\django\sad')

DomainTxt = '..\static\config\domain.txt'
f = open(DomainTxt, 'r')
print f.readlines()
f.close





