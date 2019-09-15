# -*- coding:utf-8 -*-
# @Time : 2019-09-14 14:19
# @Author：lqc
# @Email:572948875@qq.com
# File : 93_upload.pyimport win32gui

import win32con

def upload_file(filepath):
    dialog = win32gui.FindWindow("#32770", "打开") #一级窗口

    #找到窗口

    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboxEx32", None) #二级

    comboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, "Combox", None) #三级

    edit = win32gui.FindWindowEx(comBox, 0, 'Edit', None) # 文本输入窗口-四级

    button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&O)") # 四级

    # 操作

    win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath) # 发送文件路径

    win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button) # 点击打开按钮，提交文件