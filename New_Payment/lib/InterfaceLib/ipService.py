# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2022/1/17 15:23
# @Email:15018529620@163.com
# @File:ipService.py

"""
接口名称：IP地址解析服务
功能说明：通过IP地址解析该IP地址的归属国家等信息
请求地址：http://192.168.0.88:8000/payment/ipService/query
"""

from configs.config import *
import requests


class IPServer:

    def ip_service(self,ip,merchantNo='1002'):  # 1002为默认值参数，必须定义在非默认值参数后面。

        url = f'{IPHOST}/ipService/query'
        data={
            "head": {
                "requestId": "ip001",
                "tranCode": "$C(X",
                "merchantNo": merchantNo,
                "version": "1.0.0"
            },
            "body": {
                "ip": ip
            }
            }
        try:
            res = requests.post(url, json=data)
            return res.json()
        except Exception as e:
            return e




if __name__ == '__main__':
    info = IPServer().ip_service("38.199.83.78")
    print(info)