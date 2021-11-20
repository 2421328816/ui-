#-*-  coding:utf-8  -*-
#@File:1106学习.py
#@Time:2021/11/1617:43
#@site:
#@Software:PyCharm
#@Author:sfz
# print(type(1))
# print(type(1.1))
#字符
# print(round(2/3))#除法得结果都是float型
# print(4/2,type(4/2))
# print(7//2)#取整
# print(7%4)#取余
# str='晓明'
# print(str)
# a=1
# a+=1
# print(a)#python中的单引号、双引号、三引号是成对出现的，三引号是可以换行得
#
# str1='我今天' \
#      '很kaixin'
# str2='''我今天很烦、
# 很烦'''
# print(str1,str2)
# str3='dsfdsfds'
# print(str3[-5:-2])
# # print(str3[3],str3[-1],str3[-8])
# #
# # print(str3[1:2])
# # print(str3[3:])
#
# #列表 list可以存放任意数值类型，，可以增删改操作
# list1=[1,2,44,55,66,99,['小敏','小强']]
# # list2=[]
# # print(list1)
# # print(list2)
# # print(list1[3])
# #list1.remove(99)#直接删除数值
# # list1.pop(1)#不写索引，从尾部删除，写索引，删除索引的值
# # list2=list1
# list1[6]=100
# print(list1)
# #print(list1[-1][0])
# #元组 tuple () 里面可以存放任意类型  不可以增删改操作
# tuple1=(11,22,666,55,44,[10,55])
# print(tuple1[5][1])
#
# #字典，dict{key:value},不能索引和切片，key:是不可改变类型（字符串，数值、元组），value是任意，
# # 整体是可以增删改操作
# dict1={'小孩':'01','大人':'18','青年':'24'}
# print(dict1)
#
#
# str1="susan"
# # 获取:ssn
# print(str1[0]+str1[2]+str1[-1])
#
# print(str1[::-1])#步长

#数据类型有：整型、浮点型、字符串、列表、数组、字典
#布尔类型 对或错 True或者False
# print(bool(1))
# print(1==2)
#多种情况的时候，，and是且的关系，一假，为假，全真则真，同时满足，or或者一真则真，全假则假，满足其一即可
# print(1<0 or 1>0)
# print(1<0)
#如果and和or一起运算，and优先级比or高
# print(4>2 or 8<4 or 1==1 and 5<3)
# password='123456'
# if password=='123456':
#     print('密码正确')
#     print('恭喜')
# age=30
# if age>18:
#     print('你已经成年啦')
# else:
#     print('你未成年')

#打印出1-100的和
# i=1
# sumdata=0
# while i<=100:
#     sumdata+=i
#     i+=1
# print(sumdata)
#斐波那契数列,后一项是前两项的和  0 1 1 2 3 5 8 13……
# a,b=4,4+1
# print(a,b)

# i=0
# j=1
# while i<1000:
#     #print(i,end='\t')
#     i,j=j,i+j
#     print(i,j)
# alist=[11,'sdd','dd','kk']
# for i in range(len(alist)):#使用场景，while知道次数，for不知道次数
#     if i==2:
#         #continue#跳过该条数据
#         break#跳出循环
#     print(alist[i])

#1函数：把一系列动作打包在一起,使用函数，函数名（）
# 例如：登录  1打开浏览器 2输入网址  3输入用户名和密码 4点击登录
# def login():
#     print('1打开浏览器')
#     print('2输入网址')
#     print('3输入用户名和密码')
#     print('4点击登录')
# #使用函数，函数名（）,调用函数，一定要先定义后调用，作用节省代码，偷懒方便封装
# login()
# def sum(end):#end叫形参
#     sumdata=end+end
#     print(sumdata)
# sum(100)#100叫实参

#求start到end值的和
# def shuju(start,end):
#     sumdata=0
#     count=start
#     while count<=end:
#         sumdata+=count
#         count+=1
#     print(sumdata)
# shuju(1,2)

# def sum(start,end,step):
#     sumdata=0
#     count=start
#     while count<=end:
#         sumdata+=count
#         count+=step
#     #print(sumdata)
#     return sumdata
# a=sum(1,10,2)
# print(a)
#内置函数，
#print(max(1,10,52,20))

#对象方法
alist=['dd','ss','qqq']
#str1='qw'.join(alist)
print(alist)#列表转换成字符串

#列表转成字符串,split切割
# list2=str1.split('qw')
# print(list2)
#去空格，strip()
str1='  dsds  sfds  '
str2=str1.strip()
print(str2)
#replace 替代
str4=str1.replace(' ','')
print(str4)
#算法  倒叙排列  思路 第一项与最后一项索引的值交换 依次进行下去
# alist = [5,8,6,9,3,4,8,9,5,1,4,2]#定义一个列表