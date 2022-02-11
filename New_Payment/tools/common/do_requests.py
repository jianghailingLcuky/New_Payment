# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2022/1/18 10:01
# @Email:15018529620@163.com
# @File:do_requests.py

"""
封装常用的请求方法
"""
import requests
import json
import urllib3
from configs.config import *

class RequestMethod:
    def request_get(self,url,data=None,header=None):
        """
        get请求
        请求HTTPS时Requests 忽略对SSL证书的验证
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        try:
            # urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
            urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        except AttributeError as e:
            print(e)
        res = None
        if header != None:
            res = requests.get(url=url,params=data,headers=header,verity=False)   #verity=False  取消警告
        else:
            res = requests.get(url=url, params=data,verity=False)
        return res

    def request_post_data(self,url,data,header=None):
        """
        post请求：body为data格式
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        try:
            # urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
            urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        except AttributeError as e:
            print(e)
        res = None
        if header != None:
            res = requests.post(url=url, params=data, headers=header, verity=False)  # verity=False  取消警告
        else:
            res = requests.post(url=url, params=data, verity=False)
        return res.json()

    def request_post_json(self,url,data,header=None):
        """
        post请求：body为json格式
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        try:
            # urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
            urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
        except AttributeError as e:
            print(e)
        res = None
        if header != None:
            res = requests.post(url=url, params=data, headers=header, verity=False)  # verity=False  取消警告
        else:
            res = requests.post(url=url, params=data, verity=False)
        return res.json()

    def run_method(self,method,url=None,data=None,header=None,json_ge=None):
        res = None
        if method == 'post' or method == "POST":
            if json_ge == "json":
                res = self.request_post_json(url, data, header)
            else:
                res = self.request_post_data(url,data,header)
        else:
            res = self.request_get(url,data,header)
        #ensure_ascii=False防止中文乱码，sort_key根据keys的值进行排序，indent是缩进
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == '__main__':
    run =  RequestMethod()
    #接口调用
    url = f'{IPHOST}/ipService/query'
    data = {
        "head": {
            "requestId": "ip001",
            "tranCode": "$C(X",
            "merchantNo": '1002',
            "version": "1.0.0"
        },
        "body": {
            "ip": '113.156.1.199'
        }
    }
    res = run.request_post_json(url,data)
    print(res.json())


