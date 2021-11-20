#-*-  coding:utf-8  -*-
#@File:20211119ceshi.py
#@Time:2021/11/1913:20
#@site:
#@Software:PyCharm
#@Author:sfz
#异常机制
import pytest
try:
    a=int(input('请输入一个数字'))
    b=1/a
except ZeroDivisionError as e1:#0为分母异常
    print('0不能作为分母')
except ValueError as e2:
    print('您输入的不是数字')
except:
    print('程序有错误')
else:
    print('程序未报错')
finally:
    print('程序执行完毕')
import logging#日志模块
import time#时间模块
import traceback#导入异常信息模块
# logging.basicConfig(level='DEBUG',filename='./log1.log',filemode='a')
# logging.debug(time.strftime('%y-%m-%d %H:%M:%S')+'记录debug信息')
# logging.info('info级别')
# logging.warning('WARNING级别')
# logging.error('ERROR级别')
# logging.critical('CRITICAL级别')

assert 1==1#当结果为真时,断言不做事情,当结果为假时,断言会报错