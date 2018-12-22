# -*- coding:utf-8 -*-
from keywords.httpkeys import HTTP

urlauth = 'http://112.74.191.10:8081/inter/HTTP/auth'
urllogin = 'http://112.74.191.10:8081/inter/HTTP/login'
urllogout = 'http://112.74.191.10:8081/inter/HTTP/logout'
urluerinfo = 'http://112.74.191.10:8081/inter/HTTP/getUserInfo'
status = 'status'
data = None
token = ''

# 创建HTTP对象
http = HTTP()

# 无token
print('-----------------------------------无token，获取权限-----------------------------------')
http.post(urlauth)
# 断言结果
http.assertequls(status, '200')

# token为''
print('-----------------------------------token为空，获取权限-----------------------------------')
http.addheader('token',token)
http.post(urlauth)
http.assertequls(status, '200')

# token为'a'
print('-----------------------------------token为一位值，获取权限-----------------------------------')
token = 'a'
http.addheader('token', token)
http.post(urlauth)
http.assertequls(status, '200')

# token值过长
print('-----------------------------------token值过长，获取权限-----------------------------------')
token = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
http.addheader('token', token)
http.post(urlauth)
http.assertequls(status, '200')



# token未授权
print('-----------------------------------token未授权，获取权限-----------------------------------')
token = 'a8a36395f3324a298e7eea90821fc96a'
http.addheader('token', token)
http.post(urlauth)
http.assertequls(status, '200')

# 保存上一步的token值
# token = jsonresult['token']
http.saveparams('tk','token')

http.addheader('token','{tk}')
print(http.session.headers)

# # token已授权
print('-----------------------------------token已授权，获取权限-----------------------------------')
http.post(urlauth)
http.assertequls(status, '201')

# 登录用户查询用户信息
data = 'username=demo003&password=demo003'
http.post(urllogin,data)
http.assertequls(status, '200')
http.saveparams('id','userid')

data = 'id={id}'
http.post(urluerinfo,data)
http.assertequls(status, '200')


http.post(urllogout)
http.assertequls(status, '200')



