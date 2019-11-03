from robot.api import logger
from openpyxl import load_workbook

# 自测自己写的类或者模块，功能是否能够正常使用，----单元测试

class myExcelLibrary(object): # 类名与模块名保持一致
    
    “”“
    自定义的excel操作库
    所有关键字：
    ”“”

    ROBOT_LIBRARY_VERSION = 1.0
    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self, flag=None):
    	logger.info("初始化一个excel文件")
        pass

    def open_excel(self, filepath):
    	“”“
    	hello,excel,open it
    	”“”
    	logger.info("打开一个excel文件")
        pass
        
    def select_sheet(self, sheetname=None):
    	"""
    	select a sheet
    	"""
    	logger.info("选择一个表单进行操作。")
        pass
        
    def read_data(self, row, column):
		pass
		
	def add_twoNum(self, a, b):
		return int(a)+int(b)