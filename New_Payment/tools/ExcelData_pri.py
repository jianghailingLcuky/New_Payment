# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2021/9/2 8:54
# @Email:15018529620@163.com
# @File:ExcelData_pri.py

import xlrd
from xlutils.copy import copy
import pprint


#前期封装好，避免后期改动较多

#1-获取Excel数据-请求体和预期结果


def get_excel_data(sheetName,caseName):
    """
    :param sheetName:表名
    :param caseName: 用例名
    :return: 一个列表嵌套元组 [(请求体1，期望数据1)，(请求体2，期望数据2)]
    """
    resList = []    #存放结果
    excelDir = '../data/NewPayment_testcase.xls'   #使用相对目录  注意中文的编码，防止乱码
    # 1- 打开excel  formatting_info=True-保持格式样式不变
    workbook = xlrd.open_workbook(excelDir,formatting_info=True)
    # 2- 对某一个sheet进行操作（一个excel里面包含多个sheet）  可以用名字也可以用下标的方式
    workSheet = workbook.sheet_by_name(sheetName)
    # 3- 获取值  第6列和第8列
    #print(workSheet.col_values(0))   #获取整列数据-从第一行开始获取 index=0
    # 4- 获取数据，遍历数据
    print(workSheet.col_values(0))

    idx = 0  # 从下标为0行的开始
    for one in workSheet.col_values(0):
        if caseName in one:    # 单元格数据 cell （行号，列号） 从0开始
            reqBody = workSheet.cell(idx,6).value    #获取请求体
            resData = workSheet.cell(idx,8).value    #获取期望数据
            #每一行数据进行保存
            # print('每行数据-cell6： {}'.format(reqBody))
            # print('每行数据-cell8： {}\n'.format(resData))
            resList.append((reqBody,resData))
            print(resList)
        idx += 1
    #pprint.pprint(resList)
    return resList



if __name__ == '__main__':
    list = get_excel_data('1-登录模块','login')
    for a in list:
        print('**********************************')
        #print(a)


