# _*_coding:utf_8_*_
# @Author:Jiang hailing
# @Time:2022/1/7 14:12
# @Email:15018529620@163.com
# @File:ExcelData_other.py

import xlrd
class ExcelUtil():
    def __init__(self, excelPath, sheetName="Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        print(self.rowNum)
        # 获取总列数
        self.colNum = self.table.ncols
        print(self.colNum)
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1


            for i in list(range(self.rowNum-1)):
                s = {}
                # 从第二行取对应values值
                s['rowNum'] = i+2
                values = self.table.row_values(j)
                for x in list(range(self.colNum)):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
if __name__ == "__main__":
    filepath = "../data/NewPayment_testcase.xls"
    sheetName = "1-登录模块"
    data = ExcelUtil(filepath, sheetName)
    print(data.dict_data())
