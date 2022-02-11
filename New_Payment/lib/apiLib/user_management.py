# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2022/1/4 10:13
# @Email:15018529620@163.com
# @File:add_users.py

"""
接口名称：用户信息管理
功能说明：用户信息管理
请求地址：——
"""





from lib.apiLib.login import *
import requests,json




class UserManger:

    #1-新增用户
    def add_user(self,inToken,inData):
        '''
        :param inToken: 登录接口获取的token
        :param inData: 新增用户body
        :return: 返回响应内容
        '''
        url = f'{HOST}/api/user/v1/add'
        Authorization = 'Bearer ' + inToken
        #print('拼接后的Authorization为： {}'.format(Authorization))
        headers = {'Content-Type':'application/json','Authorization':Authorization}
        res = requests.post(url,headers=headers,json=inData)
        print('请求成功后的响应码为： {}\n' .format(res.status_code))
        return res.json()

    #2-查看用户详情
    def user_detail(self,inToken,user_id):
        url = f'{HOST}/api/user/v1/detail'
        Authorization = 'Bearer ' + inToken
        headers = {'Content-Type':'application/json','Authorization':Authorization}
        payload = {
    "head": {
        "version": "",
        "tranCode": "",
        "merchantNo": "",
        "requestId": ""
    },

    "body": {
        "userId": user_id
    }
}
        res = requests.post(url,headers=headers,json=payload)
        return res.json()

    #3-更新用户信息
    def user_edit(self,inToken,payload,headers=None):
        url = f'{HOST}/api/user/v1/edit'
        Authorization = 'Bearer ' + inToken
        headers = {'Content-Type': 'application/json', 'Authorization': Authorization}
        res = requests.post(url,headers=headers,json=payload)
        return res.json()


if __name__ == '__main__':
    #登录获取token
    captcha, uuid = get_verification_code()
    user_data = {
        "body": {
            "userAccount": 'wujiayao',
            "password": '535460548484wujiayao',
            "captcha": captcha,
            "uuid": uuid
        }
    }
    token = Login().login(user_data,getToken=True)
    #1-新增用户
    data = {
        "head": {
            "version": "",
            "tranCode": "",
            "merchantNo": "",
            "requestId": ""
        },
        "body": {

            "userAccount": "testjhl",  # 必填
            "userName": "jianghailing",
            "question": "111",  # 必填
            "answer": "222",  # 必填
            "realName": "jianghailing",
            "sex": 1,  # 必填  (1:男2女)
            "mobilePhone": "15018529620",
            "phone": "15018529620",
            "email": "jianghailing@dedeify.net",  # 必填
            "idType": 1,   #件类型(1：身份证2:护照3：军官证4:其它)
            "idCode": "",
            "permission": 1,  # 必填    用户所属组(1:海外2：国内)
            "province": "",
            "city": "",
            "address": "",
            "zipCode": "",
            "macAddress": "",
            "remark": "",
            "dataScope": 0,  # 必填    数据范围（0:全部数据权限1:自定数据权限）
            "roleIds": [1, 2, 4],
            "merIds": [1, 2, 3]
        }
    }
    res = UserManger().add_user(token,data)
    print('请求响应内容为：')
    print(res)


   # 2-查看用户详情
   #  for a in range(0,500):
   #  userDetail = UserManger().user_detail(token,10035)  #100234
   #  print(userDetail)

    #3-更新用户信息
    editData ={
    "head": {
        "version": "",
        "tranCode": "",
        "merchantNo": "",
        "requestId": ""
    },
    "body": {
        "userId": 10035,
        "userAccount": "jianghailingling",
        "userName": "jianghailingling",
        "question": "你的名字呢",
        "answer": "jianghailingling",
        "realName": "jianghailingling",
        "sex": 1,
        "mobilePhone": "",
        "phone": "",
        "email": "",
        "idType": 1,
        "idCode": "",
        "permission": 0,
        "province": "",
        "city": "",
        "address": "",
        "zipCode": "",
        "macAddress": "",
        "remark": "",
        "dataScope": 0,
        "roleIds": [
            0
        ],
        "merIds": [
            0
        ]
    }
}


    # userEdit = UserManger().user_edit(token,editData)
    # print(userEdit)


