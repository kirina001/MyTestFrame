# -*- coding:utf-8 -*-
import requests, json


class HTTP:
    # 构造方法
    def __init__(self):
        # session对象模拟浏览器cookie
        self.session = requests.session()
        # json解析后的结果
        self.jsonresult = {}
        # 存储所需的参数（类似于jmeter的关联变量userid）
        self.params = {}

    # 定义post方法
    def post(self, path, data=None):
        '''
        定义post方法
        :param path: url路径
        :param data: 键值对传递字符串参数
        :return: 无返回值
        '''
        if data is None:
            result = self.session.post(path)
        else:
            # 替换参数
            data = self.__getprams(data)
            # 将参数转为字典的方式传入
            data = self.__todict(data)
            result = self.session.post(path, data=data)
        self.jsonresult = json.loads(result.text)

    # 断言预期结果与实际结果是否相等
    def assertequls(self, key, value):
        '''
        断言预期结果与实际结果是否相等
        :param key: 预期结果
        :param value: 实际结果
        :return: 判定结果pass or faild
        '''
        print(self.jsonresult)
        # 判定指定关键字的值是否相等
        if str(self.jsonresult[key]) == str(value):
            print('pass')
        else:
            print('faild')

    # 添加head信息
    def addheader(self, key, value):
        value = self.__getprams(value)
        self.session.headers[key] = value

    # 保存键值对的params
    def saveparams(self, param, key):
        # 类似于 token = jsonresult['token']
        self.params[param] = self.jsonresult[key]
        print('-----------------------------------获取关联参数列表-----------------------------------')
        print(self.params)

    # 获取参数
    def __getprams(self, getparam):
        for key in self.params:
            getparam = getparam.replace('{' + key + '}', self.params[key])
        return getparam

    # 将传入的参数转换为字典
    # 转换前  data='username=demo003&password=demo003'
    # 转换后 data={'username':'demo003,'password':'demo003'}
    def __todict(self, s):
        # 存储转换为dict后的参数
        httpparam = {}
        # 用&分割参数个数
        param = s.split('&')
        for ss in param:
            # 用=分割键值对
            p = ss.split('=')
            httpparam[p[0]] = p[1]
        return httpparam
