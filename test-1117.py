#-*-  coding:utf-8  -*-
#@File:test-1117.py
#@Time:2021/11/1720:52
#@site:
#@Software:PyCharm
#@Author:sfz
# from selenium import webdriver#导入webdriver模块
# import time
# driver_path='E:\webDriver\chromedriver.exe'#webdirver所处路径
# driver=webdriver.Chrome(driver_path)
# driver.get('https://www.baidu.com')#地址url自动
# time.sleep(5)
# driver.quit()#退出

#浅拷贝与深拷贝
import copy
# list1=[10,20,30,70,50,[11,22,33]]
# list2=list1
# list1[-1][1]=99
# print(list2)#普通copy赋值，，两个表其实指向的同一个地址，一个，有一个变了，另一个也会变

#10属于子列表，不属于list1
# print(10 in list1)
#浅拷贝对于列表，指向的是不同的地址
# list01=copy.copy(list1)
# list1[2]=300
# print(list1,id(list1))
# print(list01,id(list01))
#浅拷贝等价于切片，对于子列表仍然指向的是同一个地址,
# list3=list1[:]
# list1[1]=80#指向的不同地址
# print(list3,id(list3))
# print(list1,id(list1))

# list3=list1[:]
# list1[-1][1]=80
# print(list3,id(list3))
# print(list1,id(list1))

#深拷贝
# list4=copy.deepcopy(list1)
# list1[-1][2]=999
# print(list4,id(list4))
# print(list1,id(list1))

#判断是否纯字符串、纯数字
# str1='1254g333'
# print(str1.isdigit())

#文件的读写
#open('d:/note1.txt')#方案一
# open('d:\\note1.txt')#方案二
# open(r'd:\note1.txt')
# fil1=open('d:/note1.txt')#读取一个文件，第一个参数为文件路径，第二个参数可以设置听说读写追加模式，缺省值为读
# #neirong=fil1.read()#读取整个文件内容
# neirong=fil1.readlines()#读取整个文件的内容，放到一个列表中，每行是一个元素
# #neirong=fil1.readline()#每读取一次，读取文件中的一行
# print(neirong)
# fil1.close()#从open方法读取完文件之后要加上close方法
#如果遇到jbk的报错，有两种解决方法去排查，一、修改settings中的file encoding
#二是修改文本文件的格式为ANSI

# file2=open('d:/note2.txt','w')#w写入模式，如果文件不存在，则创建文件，
# # 如果文件存在，则清空以前的内容，重新写入
# file2.write('竹杖芒鞋轻胜马，谁怕')
# file2.close()

#追加模式a
# file3=open('d:/note3.txt','a')#追加写入模式,如果没有文件，则创建文件
# file3.write('dddd')
# file3.close()

#r+,a+,w+,可以同时进行读写
#r+如果文件不存在，报错，写入时覆盖写入，注意不是清空写入
#w+如果文件不存在，会生成文件，写入时，清空之前的内容重新写入
#a+如果文件不存在，会生成文件，写入时，追加写入
# file3=open('d:/note3.txt','r+')#追加写入模式,如果没有文件，则创建文件
# file3.write('QQ')
# file3.close()

#w+,写模式，没有的创建文件，有的文件，清空写入
# file4=open('d:/note4.txt','w+')#
# file4.write('dsfdsfdsf')
# file4.close()
#
# file5=open('d:/note4.txt','a+')#
# file5.write('好的，很棒')
# file5.close()

#seek(参数1，参数2)光标偏移几位，参数2缺省为0
file6=open('d:/note4.txt','w+')
file6.seek(4)
file6.write('dgfd好的，可以啦，一星期一星期过去啦fgfdg')
file6.seek(0)
file6.close()

#打开文件方法，with open（）,不需要写close方法，，可以同时打开多个文件
with open('d:/note4.txt','w+') as file1,open('d:/note3.txt') as file2:
    print(file1.read())
    print(file2.read())