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
http.addheader('token', token)
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
http.saveparams('tk', 'token')

http.addheader('token', '{tk}')
print('-----------------------------------请求头信息-----------------------------------')
print(http.session.headers)

# # token已授权
print('-----------------------------------token已授权，获取权限-----------------------------------')
http.post(urlauth)
http.assertequls(status, '201')

print('-----------------------------------token已授权，进行登录-----------------------------------')
# 登录用户查询用户信息
data = 'username=demo005&password=demo005'
http.post(urllogin, data)
http.assertequls(status, '200')
http.saveparams('id', 'userid')

print('-----------------------------------存储userid，并获取用户信息-----------------------------------')
data = 'id={id}'
http.post(urluerinfo, data)
http.assertequls(status, '200')

# 重复登录
print('-----------------------------------重复登录-----------------------------------')
data = 'username=demo005&password=demo005'
http.post(urllogin, data)
http.assertequls(status, '405')

# 无用户名登录
print('-----------------------------------无用户名登录-----------------------------------')
data = 'password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名为空进行登录
print('-----------------------------------用户名为空进行登录-----------------------------------')
data = 'username= &password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名包含特殊字符1，进行登录
print('----------------------------------用户名包含特殊字符1，进行登录-----------------------------------')
data = 'username=#$%!@&password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名包含特殊字符2，进行登录
print('----------------------------------用户名包含特殊字符2，进行登录-----------------------------------')
data = 'username=큐〓㊚a&password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名包含特殊字符3，进行登录
print('----------------------------------用户名包含特殊字符3，进行登录-----------------------------------')
data = 'username=Wil🚣l&password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名长度为2，进行登录，进行登录
print('----------------------------------用户名长度为2，进行登录-----------------------------------')
data = 'username=Wi&password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名长度为3，进行登录
print('----------------------------------用户名长度为3，进行登录-----------------------------------')
data = 'username=Wil&password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名包含长度为16，进行登录
print('----------------------------------用户名包含长度为16，进行登录-----------------------------------')
data = 'username=widwwwwwwwwwwwww&password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名包含长度为17，进行登录
print('----------------------------------用户名包含长度为16，进行登录-----------------------------------')
data = 'username=widwwwwwwwwwwwwww&password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名包含长度过长，进行登录
print('----------------------------------用户名包含长度过长，进行登录-----------------------------------')
data = 'username=widwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww&password=demo004'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 无密码，进行登录
print('-----------------------------------密码校验问题-----------------------------------')
print('-----------------------------------无密码，进行登录-----------------------------------')
data = 'username=cc123'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码为空，进行登录
print('-----------------------------------密码为空，进行登录-----------------------------------')
data = 'username=cc1233&password='
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码包含特殊字符1，进行登录
print('-----------------------------------密码包含特殊字符1，进行登录-----------------------------------')
data = 'username=cc1233&password=#￥%a'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码包含特殊字符2，进行登录
print('-----------------------------------密码包含特殊字符2，进行登录-----------------------------------')
data = 'username=cc1233&password=큐〓㊚a'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码包含emoji表情，进行登录
print('-----------------------------------密码包含emoji表情，进行登录-----------------------------------')
data = 'username=cc1233&password=🚣adaacdfdf'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码长度为2，进行登录
print('-----------------------------------密码长度为2，进行登录-----------------------------------')
data = 'username=cc1233&password=df'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码长度为3，进行登录
print('-----------------------------------密码长度为3，进行登录-----------------------------------')
data = 'username=cc1233&password=ddf'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码长度为16，进行登录
print('-----------------------------------密码长度为16，进行登录-----------------------------------')
data = 'username=cc1233&password=ddfffffffffffff'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码长度为17，进行登录
print('-----------------------------------密码长度为17，进行登录-----------------------------------')
data = 'username=cc1233&password=ddfffffffffgffff'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码长度过长，进行登录
print('-----------------------------------密码长度过长，进行登录-----------------------------------')
data = 'username=cc1233&password=ffffffffffffffffddddddddf'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 无用户名密码字段，进行登录
print('-----------------------------------字段测试-----------------------------------')
print('-----------------------------------无用户名密码字段，进行登录-----------------------------------')
http.post(urllogin)
http.assertequls('status', '401')

# 3个字段，进行登录
print('-----------------------------------3个字段，进行登录-----------------------------------')
data = 'username=cc1233&aaa=cccc&password=ffffffffffffffffddddddddf'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名和密码错误，进行登录
print('-----------------------------------等价类测试-----------------------------------')
print('-----------------------------------用户名和密码错误，进行登录-----------------------------------')
data = 'username=cc1233&password=dddf'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名不存在，进行登录
print('-----------------------------------用户名不存在，进行登录-----------------------------------')
data = 'username=demo00000&password=123456'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 用户名密码不匹配，进行登录
print('-----------------------------------用户名密码不匹配，进行登录-----------------------------------')
data = 'username=test123456&password=123456'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# # 注销用户
# print('-----------------------------------注销用户-----------------------------------')
# http.post(urllogout)
# http.assertequls(status, '200')

# print('-----------------------------------SQL注入测试-----------------------------------')


# 用户名SQL注入，进行登录
print('-----------------------------------用户名SQL注入，进行登录-----------------------------------')
data = 'username=demo001\' or 1=1 #&password=123456'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 密码SQL注入，进行登录
print('-----------------------------------密码SQL注入，进行登录-----------------------------------')
data = 'username=demo001&password=demo001\' or 1=1 #'
http.post(urllogin, data=data)
http.assertequls('status', '401')

# 注销用户
print('-----------------------------------注销用户-----------------------------------')
http.post(urllogout)
http.assertequls(status, '200')
