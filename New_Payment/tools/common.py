# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2021/12/22 15:32
# @Email:15018529620@163.com
# @File:common.py

"""
常用的公共方法
"""


import hashlib
import random,datetime,string,time
import uuid
import urllib3
import requests
import json
import xmltodict



def get_md5(psw):
    """
    MD5加密
    """
    md5 = hashlib.md5()#创建md5对象
    md5.update(psw.encode('utf-8'))#加密方法
    return md5.hexdigest()#加密后的结果


def get_billNo():
    """
    生成的订单号=年月日时分秒+随机四位数
    """
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')  # 获取当前日期并格式化-str类型
    random_str = random.sample(string.digits, k=5)  # 防止订单号重复，后面加随机生成的四位数
    billNo = now_time + ("".join(random_str))
    return billNo


def get_amount_AE():
    """
    随机生成2位小数的金额
    """
    a = str(round(random.uniform(1, 5), 2))
    return a


def get_amount_50():
    """
    随机生成2位小数的金额
    """
    a = str(round(random.uniform(1, 50), 2))
    return a


def get_time():
    """
    获取时间
    """
    #timeshow = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))  #获取当前时间 ，并以当前格式显示
    timeshow = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return timeshow


def get_currency():
    """
    随机获取币种
    """
    currency = ["USD",'EUR','AUD','CNY']
    c = random.choice(currency)
    return c


def get_cardno():
    """
    随机获取卡种
    """
    #cardno = ['2223000000000023','5248480000201009',"6011963280099774",'373953192351004',"3528000000000007"]#'3528000000000007',
    #cardno = [ '5111111111111118', '5123450000000008']
    cardno = ['5123450000000008','5123456789012346','5506900140100305','4440000009900010','4440000042200022']
    c =random.choice(cardno)
    return c


def get_merno():
    """
    随机获取商户号
    """
    merno = ["1538","1539","1540"]
    m = random.choice(merno)
    return m


def post_request_ignore(url,body_data):
    """
    请求HTTPS时Requests 忽略对SSL证书的验证
    """
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    try:
        #urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
        urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
    except AttributeError as e :
        print(e)
    res = requests.post(url, data=body_data, verify=False)
    return res


def xmltojson(xmlstr):
    """
    XML转成JSON格式
    """
    #parse是XML的解析器
    xmlparse = xmltodict.parse(xmlstr)
    #json.dumps()是将dict转成json格式，loads()是将json转成dict格式
    #dumps()方法的ident=1格式化json(由上而下进行展示)
    jsonstr = json.dumps(xmlparse,indent=1)
    #print(jsonstr)
    return jsonstr


def create_phone():
    """
    随机创建有效手机号码
    """
    #第二位数字
    second = [3,4,5,7,8][random.randint(0,4)]
    #第三位数字
    third = {
        3:random.randint(0,9),
        4:[5,7,9][random.randint(0,2)],
        5:[i for i in range(0,10) if i !=4][random.randint(0,8)],
        7:[i for i in range(0,10) if i not in [4,9]][random.randint(0,7)],
        8:random.randint(0,9),
    }[second]
    #最后八位
    suffix = random.randint(9999999,100000000)
    #拼接手机号
    return '1{}{}{}'.format(second,third,suffix)









if __name__ == "__main__":
    get_md5('psw')          #MD5加密
    get_billNo()           #生成的订单号=年月日时分秒+随机四位数
    get_amount_AE()        #随机生成2位小数的金额- <10
    get_amount_50()        #随机生成2位小数的金额
    get_time()             #获取时间
    get_currency()         #随机获取币种
    get_cardno()           #随机获取卡种
    get_merno()            #随机获取商户号
    post_request_ignore('url', 'body_data')   #请求HTTPS时Requests 忽略对SSL证书的验证
    xmltojson('xmlstr')    #XML转成JSON格式
    create_phone()         #随机创建有效手机号码
