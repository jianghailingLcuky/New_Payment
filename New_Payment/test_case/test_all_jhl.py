# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2022/1/10 11:26
# @Email:15018529620@163.com
# @File:test_all_my.py


"""
测试pytest的使用以及allure
执行指定测试用例 --allure-severities blocker
未标记的则默认为normal
BLOCKER = 'blocker'　　阻塞缺陷
CRITICAL = 'critical'　严重缺陷
NORMAL = 'normal'　　  一般缺陷
MINOR = 'minor'　　    次要缺陷
TRIVIAL = 'trivial'　　轻微缺陷
"""
import pytest
import allure
import os


@allure.step('Users login')
# 在所需要调用的函数前面加个装饰器@pytest.fixture()
@pytest.fixture(scope="function", params=None, autouse=False, ids=None, name=None)
def login(self):
    print('执行用例前先进行登录')
    yield
    print('执行用例之后注销登录')

@allure.feature('allure.feature:Funcation')
class Test_Pytest():

    @allure.severity('critical')
    #@pytest.mark.xfail(reason='该功能尚未完成')
    def test_one(self):
        print("\n---start---")
        pytest.xfail(reason='该功能尚未完成000')
        print('test_one方法执行')
        assert 1==1

    @allure.severity('normal')
    @allure.story('story1')
    @pytest.mark.webtest
    def test_two(self):
        print('test_two方法执行')
        assert 'lin' not in 'loveln'

    # reruns:最大重试次数，reruns_delay:重试间隔时间，单位是秒; R表示用例失败后正在重试，尝试5次。

    @allure.severity('minor')
    @allure.story('story2-功能点描述')
    @allure.description('description-测试用例描述')
   # @pytest.mark.flaky(reruns=5,reruns_delay=2)
    def test_three(self):
        print('case3:test_step')
        #login()
        with allure.step('step 2'):
            allure.attach('apple','f1')
            allure.attach('Cherry','f2')
        with allure.step('step 3'):
            pass
        with allure.step('step 4:Verification results'):
            allure.attach('success-1','expext-1')
            allure.attach('fail-2','expext-2')
            assert 'success' == 'success'
        assert 3-2==1

    def test_three_01(self):
        print('test_three_01')
        name = 'jhl'
        assert name in '123jhl'


    def test_three_02(self):
        print('test_three_02')
        assert hasattr('2','123')

if __name__ == '__main__':

    # 生成的报告是json格式数据，无法直观的查看测试结果，执行以下命令将数据转化为图形界面
    # allure  generate. / < 测试生成的数据 > / -o. / < 测试报告存放的路径 > / --clean
    # –clean目的是先清空测试报告目录，再生成新的测试报告。
    pytest.main(['test_all_jhl.py','-s','-v','--alluredir', '../report/temp'])   #< 测试生成的数据 >
    os.system('allure generate ../report/temp -o ../report/reports --clean')
    #pytest.main(['test_all_jhl.py','-s'])
    #pytest.main(['-s','-r','test_all_jhl.py','test_all_my.py'])

    # 运行指定用例
    # pytest test_all_my.py::class_Pytest::test_one
    # pytest.main(['-s','test_all_jhl.py','-m=webtest'])  #执行标记为webtest的用例  或 not webtest

    # # 缩短脚本运行的时长，使用多进程来执行cases
    #pytest.main(['-s','-r','test_all_jhl.py','-n 2']) # NUM为并发的进程数

    #重试机制
    #pytest.main(['-s','-r','test_all_jhl.py','--reruns 2'])

    #执行筛选的用例--语法使用有问题，待确认
    # pytest.main(['test_all_jhl.py','-s','-v','-k','three or two','--collect-only','--alluredir','../report/temp'])
    # os.system('allure generate ../report/temp -o ../report/reports --clean')
