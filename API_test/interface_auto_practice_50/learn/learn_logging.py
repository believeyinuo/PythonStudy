# -*- coding: utf-8 -*-
# @Time : 2019-08-29 10:59
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : learn_logging.py
# @Project : API_test

import logging

# logger  收集日志
# handler 输出日志  指定的文件还是控制台 默认到控制台

# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# 定义一个日志收集器 my_logger
my_logger = logging.getLogger("python11")

# 设定级别
my_logger.setLevel('DEBUG')

# 设置日志输出格式
# %(name)s              Logger的名字
# %(levelno)s           数字形式的日志级别
# %(levelname)s         文本形式的日志级别
# %(pathname)s          调用日志输出函数的模块的完整路径名，可能没有
# %(filename)s          调用日志输出函数的模块的文件名
# %(module)s            调用日志输出函数的模块名
# %(funcName)s          调用日志输出函数的函数名
# %(lineno)d            调用日志输出函数的语句所在的代码行
# %(created)f           当前时间，用UNINX标准的表示时间的浮点数表示
# %(relativeCreated)d   输出日志信息时的，自Logger创建以来的毫秒数
# %(asctime)s           字符串形式的当前时间，默认格式是"2003-07-08 16:49:45,896".逗号后面是毫秒数
# %(thread)d            线程ID，可能没有
# %(threadName)s        线程名，可能没有
# %(process)d           进程ID，可能没有
# %(message)s           用户输出的消息
formater = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

# 输出日志 创建一个自己的输出渠道
ch = logging.StreamHandler()
ch.setLevel('DEBUG')
ch.setFormatter(formater)

fh = logging.FileHandler('learn_logging.txt', encoding='utf-8')
fh.setLevel('DEBUG')
fh.setFormatter(formater)

# 两者对接
my_logger.addHandler(ch)
my_logger.addHandler(fh)

# 收集日志
my_logger.debug("debug")
my_logger.error("error")


