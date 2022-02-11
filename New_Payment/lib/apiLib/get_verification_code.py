# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2021/12/21 14:10
# @Email:15018529620@163.com
# @File:get_verification_code.py



"""
接口名称：获取登录验证码
功能说明：获取登录验证码
请求地址：/captcha
"""

import requests,pprint,json
from configs.config import HOST


def get_verification_code():
    url = '{}/captcha'.format(HOST)
    res = requests.post(url)
    #将响应内容转成json  json.loads()
    # resData = res.text
    # resData = json.loads(resData)
    #print(res.text)
    resData = res.json()
    """
    首先执行try部分，如果try报错，就会执行except部分，没有报错就会跳过except部分
    """
    try:
        captcha = resData["data"]["captcha"]
        uuid =resData["data"]["uuid"]
        #print("captcha:{},\nuuid:{}".format(captcha,uuid))
        return captcha,uuid
    except :
        captcha = '未获取到验证码'
        uuid = '未获取到UUID'
        return captcha,uuid


if __name__ == '__main__':
    captcha,uuid = get_verification_code()
    print(captcha,uuid)
    # print(type(msg))
    # print(msg)
