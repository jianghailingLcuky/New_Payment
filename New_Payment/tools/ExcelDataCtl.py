#-*- coding: utf-8 -*-
#@File    : ExcelDataCtl.py
#@Time    : 2020/10/26 21:35
#@Author  : xintian
#@Email   : xxx@qq.com
#@Software: PyCharm
#有圈的是包，没有圈的是文件夹
'''
完成读取数据的操作 或 其他操作
所有的数据处理都在方法里面处理好，不能放在测试类处理
'''

import xlrd
from xlutils.copy import copy
import json

#1- 获取excel数据---请求体+预期结果
def get_excel_data(sheetName,caseName):
    '''
    :param sheetName: 表名
    :param caseName: 用例名
    :return: 一个列表嵌套元组   [(请求体1，期望数据1),(请求体2，期望数据2)]
    '''
    resList = []#放结果的
    excelDir = '../data/在线考试系统接口测试用例-v1.3.xls'
    #1- 打开excel对象---formatting_info=True  保持样式
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)
    #2- 对某一个sheet操作
    workSheet = workBook.sheet_by_name(sheetName)
    #3- 获取值  第6列 和第8列
    # print(workSheet.col_values(0))

    #4- 获取数据
    idx = 0#从第0行开始操作-也可以从第1行（根据实际sheet）
    for one in workSheet.col_values(0):
        if caseName in one:#说明这条用例使我们需要的
            #请求体--单元格数据--cell(行号，列号)0从0开始
            reqBody = workSheet.cell(idx,6).value  #字符串
            respData = workSheet.cell(idx, 8).value#期望数据
            reqBody = json.loads(reqBody)   #字符串转字典
            respData = json.loads(respData) #字符串转字典
            #每一行数据增加返回list里
            resList.append((reqBody,respData))  #拿到的为字典，可以进行键的取值  ，单引号；若为字符串，则为双引号
        idx += 1#每次遍历一次，就准备操做下一行
    return resList



if __name__ == '__main__':
    res = get_excel_data('1-登录模块','login')
    for one in res:
        print(one)
