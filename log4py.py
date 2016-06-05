# /usr/bin/env python
# coding=utf-8
# 日志记录的模块
# 2016-6-4 by lipper
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log/test.log',
                    filemode='a+')


# 将info按level写入日志
def log_debug(info):
    logging.debug(info)


def log_info(info):
    logging.info(info)


def log_warning(info):
    logging.warning(info)


def log_error(info):
    logging.error(info)


def log_critical(info):
    logging.critical(info)

level = {'debug': log_debug, 'info': log_info, 'warning': log_warning, 'error': log_error, 'critical': log_critical}

# level['debug']('this is a test.')
