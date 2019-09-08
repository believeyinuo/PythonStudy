# -*- coding: utf-8 -*-
# @Time : 2019-08-29 12:05
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : do_logging.py
# @Project : API_AUTO_test

import logging
from API_AUTO_test.interface_auto_practice_50.tools import project_path


class MyLog:
    def my_log(self, msg, level):
        # 定义一个日志收集器 my_logger
        my_logger = logging.getLogger("python11")

        # 设定级别
        my_logger.setLevel('DEBUG')

        formater = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        # 输出日志 创建一个自己的输出渠道
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formater)

        fh = logging.FileHandler(project_path.log_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formater)

        # 两者对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        # 收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        # 关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log(msg, 'DEBUG')

    def info(self, msg):
        self.my_log(msg, 'INFO')

    def warning(self, msg):
        self.my_log(msg, 'WARNING')

    def error(self, msg):
        self.my_log(msg, 'EERROR')

    def critical(self, msg):
        self.my_log(msg, 'CRITICAL')


if __name__ == '__main__':
    MyLog().my_log('日志1', 'ERROR')
    MyLog().my_log('日志2', 'ERROR')
    MyLog().my_log('日志3', 'ERROR')
    MyLog().debug("debug")