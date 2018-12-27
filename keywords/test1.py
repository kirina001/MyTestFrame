# -*- coding:utf-8 -*-

from keywords.httpkeys import HTTP
import inspect
# 方法名
strs = 'post'
equl = 'assertequls'
http = HTTP()

# 反射
fun = getattr(http, strs)
fun('http://112.74.191.10:8081/inter/HTTP/auth')

fun = getattr(http, equl)
fun('status', '200')

# 获取函数参数
args = inspect.getfullargspec(fun).__str__()
# 截取获取到的参数
args = args[args.find('args')+5:args.find(', varargs')]
# 把参数转为列表
args = eval(args)
# 移除self参数
args.remove('self')

print(args)
print(len(args))
print(fun.__doc__)





