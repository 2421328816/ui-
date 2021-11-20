#-*-  coding:utf-8  -*-
#@File:test02.py
#@Time:2021/11/1818:53
#@site:
#@Software:PyCharm
#@Author:sfz

# def fun1(a,b):
#     return a+b
# print(fun1(5,6))
class Ceshi:
    __a = 111  # 私有属性,在属性的前面加__就是私有属性
    def __init__(self):
        pass
    def __wanmei(self):#在，方法前加__就是私有方法
        print('这是一个私有方法')
    #私有方法和私有属性，都不能被外部直接访问，，也不能被子类直接继承
    def aabbcc(self):
        print(self.__a)#私有属性可以被类当中的方法访问
        self.__wanmei()#私有方法可以被类当中的其他方法使用访问
cl1=Ceshi()
cl1.aabbcc()

