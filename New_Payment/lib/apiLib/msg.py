#-*- coding: utf-8 -*-
#@File    : msg.py
#@Time    : 2020/10/26 21:14
#@Author  : xintian
#@Email   : xxx@qq.com
#@Software: PyCharm

#增加留言
import requests
from configs.config import HOST
from lib.apiLib.login import Login
from lib.apiLib.login import Login


#1- 封装类
class Msg:
    #1- 增加留言
    def add_msg(self,inToken,inData):
        '''
        :param inToken: 登录接口获取的token
        :param inData: 留言新增的body
        :return: 响应体
        '''
        url = f'{HOST}/api/message'
        #请求头--需要带token---格式是字典  {键：值}
        header = {'X-AUTH-TOKEN':inToken,'Content-Type':'application/json'}
        payload = inData
        resp = requests.post(url,json=payload,headers=header)
        return resp.json()





if __name__ =='__main__':
    #①登录,登录实例化并使用其里面的方法Login()
    token = Login().login({'username':'test','password':'sdgwq235'},getToken=True)
    #②增加留言
    res = Msg().add_msg(token,{'title':"九月",'content':'九月，你好'})

















#测试下
if __name__ == '__main__':
    #1- 登录操作--获取token
    token = Login().login({'username': '20154084', 'password': '123456'},getToken=True)
    #2- 新增留言接口
    info = {"title": "留言标题sq","content": "留言内容"}
    res = Msg().add_msg(token,info)
    print(res)#这个留言的id  作为后续的删除 回复操作




























