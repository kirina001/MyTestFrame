# -*- coding:utf-8 -*-
from keywords.httpkeys import HTTP

urlauth = 'http://112.74.191.10:8081/inter/HTTP/auth'
urllogin = 'http://112.74.191.10:8081/inter/HTTP/login'
urlreg = 'http://112.74.191.10:8081/inter/HTTP/register'
urllogout = 'http://112.74.191.10:8081/inter/HTTP/logout'
status = 'status'
data = None

# 创建HTTP对象
http = HTTP()
# 无token进行注册
print('-----------------------------------无token进行注册-----------------------------------')
data = 'username=testdemo002&pwd=testdemo002&nickname=testdemo002'
http.post(urlreg, data=data)
http.assertequls(status, '406')

# 添加头信息 ,token为空进行注册
print('-----------------------------------token值为空，进行注册-----------------------------------')
http.addheader('token', '')
data = 'username=testdemo002&pwd=testdemo002&nickname=testdemo002'
http.post(urlreg, data=data)
http.assertequls(status, '406')

# token值长度长度为1,进行注册
print('-----------------------------------token值长度为1，进行注册-----------------------------------')
http.addheader('token', 'a')
data = 'username=testdemo002&pwd=testdemo002&nickname=testdemo002'
http.post(urlreg, data=data)
http.assertequls(status, '406')

# token值长度过长，进行注册
print('-----------------------------------token值长度过长，进行注册-----------------------------------')
http.addheader('token', 'dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd')
data = 'username=testdemo002&pwd=testdemo002&nickname=testdemo002'
http.post(urlreg, data=data)
http.assertequls(status, '406')

# token未授权
print('-----------------------------------token未授权，进行注册-----------------------------------')
http.addheader('token', 'e8e9c1949d2a486b9c7403106c5648f4')
data = 'username=testdemo002&pwd=testdemo002&nickname=testdemo002'
http.post(urlreg, data=data)
http.assertequls(status, '406')

# 保存token信息
print('-----------------------------------保存token信息-----------------------------------')
http.post(urlauth)
http.assertequls(status, '200')
http.saveparams('t', 'token')
http.addheader('token', '{t}')

# 已授权token，进行注册
print('-----------------------------------已授权token，进行注册-----------------------------------')
data = 'username=bbb0004&pwd=bbb0004&nickname=bbb0002&describe=ccccc'
http.post(urlreg, data=data)
http.assertequls(status, '200')

# 无用户名，进行注册
print('-----------------------------------用户名校验-----------------------------------')
print('-----------------------------------无用户名，进行注册-----------------------------------')
data = 'pwd=testdemo004&nickname=testdemo004'
http.post(urlreg, data=data)
http.assertequls(status, '401')

# 用户名为空，进行注册
print('-----------------------------------用户名为空，进行注册-----------------------------------')
data = 'username= ''&pwd=testdemo004&nickname=testdemo004'
http.post(urlreg, data=data)
http.assertequls(status, '401')

# 用户名重复，进行注册
print('-----------------------------------用户名已注册，再次进行注册-----------------------------------')
data = 'username=demo006&pwd=demo006&nickname=testdemo004'
http.post(urlreg, data=data)
http.assertequls(status, '401')

# 用户名为特殊字符1，进行注册
print('-----------------------------------用户名为特殊字符1，进行注册-----------------------------------')
data = 'username=$%$&pwd=testdemo004&nickname=testdemo004'
http.post(urlreg, data=data)
http.assertequls(status, '401')

# 用户名为特殊字符2，进行注册
print('-----------------------------------用户名为特殊字符2，进行注册-----------------------------------')
data = 'username=큐〓㊚&pwd=testdemo004&nickname=testdemo004'
http.post(urlreg, data=data)
http.assertequls(status, '401')

# 用户名为特殊字符3，进行注册
print('-----------------------------------用户名为特殊字符3，进行注册-----------------------------------')
data = 'username=Wil🚣lllll&pwd=testdemo004&nickname=testdemo004'
http.post(urlreg, data=data)
http.assertequls(status, '401')

# 用户名长度为2，进行注册
print('-----------------------------------用户名长度为2，进行注册-----------------------------------')
data = 'username=cc&pwd=testdemo004&nickname=testdemo004'
http.post(urlreg, data=data)
http.assertequls(status, '401')

# 用户名长度为3，进行注册
print('-----------------------------------用户名长度为3，进行注册-----------------------------------')
data = 'username=ccc&pwd=testdemo004&nickname=testdemo004'
http.post(urlreg, data=data)
http.assertequls(status, '401')


print('-----------------------------------注销用户-----------------------------------')
http.post(urllogout)
http.assertequls(status, '200')
