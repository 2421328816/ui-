#-*-  coding:utf-8  -*-
#@File:ceshi03.py
#@Time:2021/11/1820:27
#@site:
#@Software:PyCharm
#@Author:sfz
#冒泡排序
# a=[1,8,5,2,1,3,9,6,0,52,9]
# a.sort()#永久排序
# a.sort(reverse=True)#永久排序且倒序
# print(a)
# print(sorted(a))#临时排序
# print(a[::-1])#只翻转不排序
import math
#写一个三角形的类，有初始化方法，周长方法，面积方法
class Sanjiaoxin:

    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def zhouchang(self):

        if self.a+self.b<=self.c or self.a+self.c<self.b or self.b+self.c<self.a:
            return ('无法构成三角形，忽略周长')
        else:
            return  self.a+self.b+self.c
    def mianji(self):

        if self.a + self.b <= self.c or self.a + self.c < self.b or self.b + self.c < self.a:
            return ('无法构成三角形，忽略周长')
        else:
            p = (self.a + self.c + self.b)/2
            return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
sjx=Sanjiaoxin(5,9,6)
print(sjx.mianji())


