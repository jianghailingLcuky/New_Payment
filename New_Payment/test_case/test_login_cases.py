# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2022/1/7 14:46
# @Email:15018529620@163.com
# @File:test_login_cases.py

from lib.apiLib.get_verification_code import *
from lib.apiLib.login import *
import unittest
import pytest
import os
import allure
import json
import shutil

"""
登录测试，其他接口使用ddt模式

测试pytest的使用以及allure
执行指定测试用例 --allure-severities blocker
未标记的则默认为normal
BLOCKER = 'blocker'　　阻塞缺陷
CRITICAL = 'critical'　严重缺陷
NORMAL = 'normal'　　  一般缺陷
MINOR = 'minor'　　    次要缺陷
TRIVIAL = 'trivial'　　轻微缺陷
"""


@allure.feature('登录测试')
class TestLogin:

    @allure.story('登录测试1-登录成功')
    @allure.severity('blocker')  #critical
    #@pytest.mark.skip  #跳过这个测试用例
    def test_login_success(self):
            captcha, uuid = get_verification_code()
            data = {
                "body": {
                    "userAccount": 'wujiayao112',
                    "password": 'wujiayao112',
                    "captcha": captcha,
                    "uuid": uuid
                }
            }
            # 实例化对象
            res = Login().login(data, getToken=False)
            assert res['code'] == '200'
            assert '成功' in res['msg']

    @allure.story('登录测试2-账户错误')
    @allure.severity('normal')
    #@pytest.mark.skip  #跳过这个测试用例
    def test_login_useraccount(self):
            captcha, uuid = get_verification_code()
            data = {
                "body": {
                    "userAccount": 'wujiayao1120',
                    "password": 'wujiayao112',
                    "captcha": captcha,
                    "uuid": uuid
                }
            }
            # 实例化对象
            res = Login().login(data, getToken=False)
            assert res['code'] == 'AC_1001'
            assert '密码错误' in res['msg']

    @allure.story('登录测试3-密码错误')
    @allure.severity('normal')
    #@pytest.mark.skip  #跳过这个测试用例
    def test_login_password(self):
            captcha, uuid = get_verification_code()
            data = {
                "body": {
                    "userAccount": 'wujiayao112',
                    "password": '123456',
                    "captcha": captcha,
                    "uuid": uuid
                }
            }
            # 实例化对象
            res = Login().login(data, getToken=False)
            assert res['code'] == 'AC_1001'
            assert '密码错误' in res['msg']

    @allure.story('登录测试4-验证码错误')
    @allure.severity('normal')
    # @pytest.mark.skip  #跳过这个测试用例
    def test_login_captcha(self):
        captcha, uuid = get_verification_code()
        data = {
            "body": {
                "userAccount": 'wujiayao112',
                "password": '123456',
                "captcha": '55',
                "uuid": uuid
            }
        }
        # 实例化对象
        res = Login().login(data, getToken=False)
        assert res['code'] == 'AC_1005'
        assert '验证码错误' in res['msg']



if __name__ == "__main__":
    #清空文件夹下的文件   # os.mkdir('要清空的文件夹名')
    shutil.rmtree('../report/temp')
    shutil.rmtree('../report/reports')
    #生成测试数据-数据为json格式
    pytest.main(['test_login_cases.py','-v','-s','--alluredir','../report/temp'])
    #将生成的测试数据转为图形界面；
    #--clear 的作用为先清空测试报告目录，再生成新的测试报告
    os.system('allure generate ../report/temp -o ../report/reports --clear')
    #pytest.main(['test_login_cases.py', '-v', '-s'])

    # suite = unittest.TestSuite()
    # #执行测试-所有用例
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #unittest.main()



