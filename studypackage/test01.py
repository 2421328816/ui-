#-*-  coding:utf-8  -*-
#@File:test-包内置函数.py
#@Time:2021/11/1818:30
#@site:
#@Software:PyCharm
#@Author:sfz
#如果文件夹里面有一个_init_.py,它就是包，当有人加载某个包时，_init_.py就会自己执行一次
import math
# print(math.sqrt(4))#求平方根
# print(math.e)
# print(math.pi)
# if __name__ == '__main__':
#     #这个分支语句，只在本模块内执行

#导入模块的的几个方法
import copy#import 模块名
#import test01
#对于同一个目录下的模块,如果遇到红色波浪线,可以选择Mark Directory as→Source Root,加 入到标准路径
# 对于灰色波浪线,可以选择右下角的小侦探图标,将进度条向左移动,就可以取消
from studypackage import test02#from 包 import 模块
from studypackage.test02 import fun1#from 包.模块 import 函数
from studypackage.test02 import * #导入该模块下的所有函数
from studypackage.test02 import fun1 as f1#不同模块中的函数出现同名的问题，取别名
from studypackage.ceshi import fun1
#同时导入多个模块内的函数，中间用逗号隔开
from studypackage.ceshi import fun1,fun2
import json
data='''
{
"aa":"tom",
"bb":"ww",
"cc":"ll"
}'''
# data1=json.loads(data)#从变量中将json格式的字符串转为字典
# print(data1)
# data2=json.dumps(data1)#将字典转为json格式的字符串
# print(data2,type(data2))
# with open('d:/note3.txt','r') as file1:
#     data2=json.load(file1)#将json格式的字符串转为字典
#     print(data2['aa'])
with open('d:/json3_2.txt','w') as file2:
    json.dump(data,file2) #将字典转为json并写入文件中