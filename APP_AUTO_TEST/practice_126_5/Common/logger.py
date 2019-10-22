# -*- coding: utf-8 -*-
# @Time : 2019/10/22 8:30 下午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : logger.py
# @Project : PythonStudy

import logging
import time
from logging.handlers import RotatingFileHandler
from APP_AUTO_TEST.practice_126_5.Common import dir_config

fmt = "%(asctime)s %(levelname)s %(filename)s %(funName)s [ line:%(lineno)d ] %(message)s"
datefmt = '%a, %d %b %Y %H:%M:%S'

handler_1 = logging.StreamHandler()

curTime = time.strftime("%Y-%m-%d %h%M", time.localtime())

# , encoding=
handler_2 = RotatingFileHandler(dir_config.logs_dir+"/Web_Autotest_{0}.log".format(curTime), backupCount=20)

# 设置rootlogger 的输出内容形式，输出渠道
logging.basicConfig(format=fmt, datafmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])

logging.info("hehehe")

















