#-*- coding: utf-8 -*-
#@File    : login.py
#@Time    : 2020/10/26 20:22
#@Author  : xintian
#@Email   : xx@qq.com
#@Software: PyCharm


from configs.config import HOST
import requests
from tools.common import *
import pprint
from lib.apiLib.get_verification_code import *



"""
接口名称：管理后台登录
功能说明：管理后台登录
请求地址：/login
"""



'''
#发请求
data---一般是表单    application/x-www-form-urlencoded   直接使用字典提交
json---  json格式   application/json   json.dumps()函数将字典转为JSON串
files---文件
'''


#登录类
class Login:

    def login(self,data,getToken=True):#实例方法    getToken=False 定义形参，默认不获取token，为了方便测试登录的接口
        # 1- 接口的url
        url = f'{HOST}/login'  # 字符串，f是3.6以后版本的format格式，
        # 2-构建请求
        #payload = inData# 请求体 body
        # captcha, uuid = get_verification_code()
        # data = {
        #     "body": {
        #         "userAccount": userAccount,
        #         "password": password,
        #         "captcha": captcha,
        #         "uuid": uuid
        #     }
        # }

        resp = requests.post(url,json=data)
        print(type(resp.json()))
        print(resp.text)
        # code = resp.json()['code']
        # print('code : {}'.format(code))
        # 3-获取token
        if getToken:
            return resp.json()['data']['access_token']
        else:
            return resp.json() # 返回是字典格式


if __name__ == '__main__':

    # userAccount = 'wujiayao'
    # password = '535460548484wujiayao'
    captcha, uuid = get_verification_code()
    data = {
        "body": {
            "userAccount": 'wujiayao112',
            "password": 'wujiayao112',
            "captcha": captcha,
            "uuid": uuid
        }
    }
    #实例化对象
    res=Login().login(data,getToken=False)    #根据实例对象的需求来确认是否需要返回token值
    code = res['code']
    print(code)
    print(type(res))








