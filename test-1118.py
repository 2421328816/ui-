#-*-  coding:utf-8  -*-
#@File:test-1118.py
#@Time:2021/11/1813:20
#@site:
#@Software:PyCharm
#@Author:sfz
#字典，键只能时不可变对象，值可以时任意对象
# dict1={'a':'A','b':'B','c':'C'}
# dict1['d']='D'#当键不在字典中时，执行新增操作
# dict1['a']='Az'#当键存在字典中时，执行修改操作
# print(dict1)#

#修改操作也可以执行，update,修改多个键值对,键不存在字典的，在最后面增加
# dict1.update({'a':'Add','b':'Bddd','e':'EED'})
# print(dict1)

#删除字典中的键值对
# del dict1['a'],dict1['c']
# print(dict1)
#
#字典的特性3，键时唯一的，特性1，无序性，特性2字典可以存放哪些数据类型? 键可以存放int型,float型,str型,元组;不可以存放列 表,字典

# 原始字符串 Jack Green , 21 ; Mike Mos, 9;
#预期修改后的字符串 # Jack Green : 21; # Mike Mos : 09;
# str1='Jack Green , 21 ; Mike Mos, 9;'
# str2=str1.split(';')[0:2]
# for one in str2:
#     name,age=one.split(',')
#     name=name.strip()
#     age=age.strip()
#     # print(name)
#     # print(age)
#     print(f'{name:<10}:{age:>02};')

# ('2017-03-13 11:50:09', 271, 131),
# ('2017-03-13 11:50:19', 271, 126),
# ('2017-03-13 11:50:25', 271, 85),
# { # 131: [
# {'lessonid': 271, 'checkintime': '2017-03-13 11:50:09'},
# {'lessonid': 273, 'checkintime': '2017-03-14 10:52:19'},
# ],
# 126: [
# {'lessonid': 271, 'checkintime': '2017-03-13 11:50:19'},
# ],
# }
# dict1={}
# dict2={}
# file_path='d:/note5.txt'
# with open('d:/note5.txt') as file1:
#     list1=file1.read().splitlines()#splitlines按照行（'\r','\r\n','\n'）分割，
#     # 返回一个包含各行作为元素的列表如果[keepends]为False不包含换行符，如果为True，则保留换行符，
#     #print(list1)
#     for one in list1:
#         list2=one.strip('(').replace(')','')
#         checkintime,lessonid,studentid=list2.split(',')[0:-1]
#         checkintime=checkintime.strip("'")
#         lessonid=lessonid.strip()
#         studentid=studentid.strip()
#
#         print(checkintime, lessonid, studentid)
#         dict2={'lessonid':lessonid,'checkintime':checkintime}
#         if studentid not in dict1:
#             dict1[studentid]=[]
#         dict1[studentid].append(dict2)
# import pprint
# pprint.pprint(dict1)
#print(checkintime,lessonid,studentid)
#所有的第三方库,默认安装在python安装目录下的lib\site-packages
#99乘法表
#方法一
# with open('d:/note2.txt','w+') as file1:
#     for i in range(1,10):
#         for j in range(1,i+1):
#             file1.write(f'{j}*{i}={j*i}\t')
#         file1.write('\n')
#方法2
with open('d:/note1.txt','w+') as file1:
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j}*{i}={j*i}\t',end='',file=file1)
        if i<9:
            print('',file=file1)