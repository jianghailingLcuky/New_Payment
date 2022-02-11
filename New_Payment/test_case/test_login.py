#-*- coding: utf-8 -*-
#@File    : test_login.py
#@Time    : 2020/10/26 21:29
#@Author  : xintian
#@Email   : xx@qq.com
#@Software: PyCharm

from tools.ExcelData_pri import get_excel_data
import pytest
from lib.apiLib.login import Login
import os

#1- 获取excel数据---请求体+预期结果
#resList = get_excel_data('1-登录模块','login')
#2- 数据传入接口代码--请求体
#3- 写入测试结果  pass/fail   预期结果与实际结果对比

#1-登录的测试类

class TestLogin:
    #加一个装饰器，进行数据驱动；如果自己开发，则需要进行for
    @pytest.mark.parametrize ("inBody","exData",get_excel_data('1-登录模块','login'))   #请求参数，期望数据,三组数据
    def test_login(self,inBody,exData):
        #2-调用登录的接口代码
        res =Login().login(inBody,getToken=True)   #res获取的是响应--格式为字典
        #3-预期结果与实际结果对比
        print(res)
        #assert res["message"] == exData


if __name__ == "__main__":
    """
    1-框架执行后的结果数据  --alluredir   存放结果数据
    2-会用Allure应用，打开结果数据
    3-浏览器去访问
    F--断言失败
    E--语法错误，有异常
    .--成功
    -s  控制台显示打印信息,其他参数请参考API文档

    """
    # 1-框架执行后的结果数据  --alluredir   存放结果数据 后面接存放的位置
    # pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    # #2-会用Allure应用，打开结果数据
    # os.system('allure server ../report/tmp')    #已设置了环境变量，因而可直接访问,启动服务   不要使用360，一般使用火狐或谷歌--设置默认浏览器

    #3-浏览器去访问































