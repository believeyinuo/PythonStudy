# -*- coding:utf-8 -*-
# @Time : 2019-08-27
# @Author：lqc
# @Email:572948875@qq.com
# File : do_excel.py

from openpyxl import load_workbook
from PythonStudy.interface_auto_practice_50.tools.read_config import ReadConfig
from PythonStudy.interface_auto_practice_50.tools import project_path


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

    # @staticmethod
    def do_excel(self):
        wb = load_workbook(self.file_name)
        mode = eval(ReadConfig.get_config(project_path.case_config_path, 'MODE', 'mode'))

        headers = self.get_headers()
        result = []

        for key in mode:  # 遍历这个存在配置文件里面的字典
            sheet = wb[key]  # 表单名
            if mode[key] == 'all':
                for i in range(2, sheet.max_row + 1):
                    data = {}
                    data["case_id"] = sheet.cell(i, 1).value
                    data["title"] = sheet.cell(i, 3).value
                    data["url"] = sheet.cell(i, 4).value
                    data["data"] = sheet.cell(i, 5).value
                    data["method"] = sheet.cell(i, 6).value
                    data["expected"] = sheet.cell(i, 6).value
                    data["sheet_name"] = key
                    # for j in range(1, sheet.max_column + 1):
                    #     data[headers[j - 1]] = sheet.cell(i, j).value
                    result.append(data)
            else:
                for case_id in mode[key]:
                    data = {}
                    data["case_id"] = sheet.cell(case_id + 1, 1).value
                    data["title"] = sheet.cell(case_id + 1, 3).value
                    data["url"] = sheet.cell(case_id + 1, 4).value
                    data["data"] = sheet.cell(case_id + 1, 5).value
                    data["method"] = sheet.cell(case_id + 1, 6).value
                    data["expected"] = sheet.cell(case_id + 1, 6).value
                    data["sheet_name"] = key
                    # for j in range(1, sheet.max_column + 1):
                    #     data[headers[j - 1]] = sheet.cell(i, j).value
                    result.append(data)

        return result

    @staticmethod
    def write_back(file_name, sheet_name, i, result, TestResult):
        wb = load_workbook(file_name)
        sheet = wb[sheet_name]
        sheet.cell(i, 8).value = result
        sheet.cell(i, 9).value = TestResult
        wb.save(file_name)


if __name__ == "__main__":
    # /Users/szdl/Desktop/PythonStudy/PythonStudy/interface_auto_practice_50/test_data/interface_auto_practice.xlsx
    # /Users/szdl/Desktop/PythonStudy/PythonStudy/interface_auto_practice_50/run.py
    print(DoExcel(project_path.test_case_path, "python").do_excel())
