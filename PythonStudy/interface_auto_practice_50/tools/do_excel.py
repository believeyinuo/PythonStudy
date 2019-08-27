# -*- coding:utf-8 -*-
#@Time : 2019-08-27 
#@Author：lqc
#@Email:572948875@qq.com
#File : do_excel.py

from openpyxl import load_workbook
# 相对路径 绝对路径
# wb = load_workbook(r"/Users/LiQingChun/Desktop/PythonStudy/PythonStudy/interface_auto_practice_50/test_data/interface_auto_practice.xlsx")
# wb1 = load_workbook("../test_data/interface_auto_practice.xlsx")


class DoExcel:
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name

    def get_headers(self):
        wb = load_workbook(self.file_name)
        sheet = wb[self.sheet_name]
        headers = []
        for i in range(1, sheet.max_column + 1):
            headers.append(sheet.cell(1, i).value)
        return headers

    def do_excel(self):
        wb = load_workbook(self.file_name)
        sheet = wb[self.sheet_name]

        headers = self.get_headers()
        result = []
        for i in range(2, sheet.max_row + 1):
            data = {}
            for j in range(1, sheet.max_column + 1):
                data[headers[j - 1]] = sheet.cell(i, j).value
            result.append(data)
        return result

    def write_back(self, i, value):
        wb = load_workbook(self.file_name)
        sheet = wb[self.sheet_name]
        sheet.cell(i, 8).value = value
        wb.save(self.file_name)


if __name__ == "__main__":
    print(DoExcel("interface_auto_practice.xlsx", "python").do_excel())