# -*- coding:utf-8 -*-
import requests, json











# 代码应该可以优化
session = requests.session()
jsonresult = {}
token = None
urlauth = 'http://112.74.191.10:8081/inter/HTTP/auth'
urlreg = 'http://112.74.191.10:8081/inter/HTTP/register'
urlout = 'http://112.74.191.10:8081/inter/HTTP/logout'
data1 = None
data2 = {}
