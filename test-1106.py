#-*-  coding:utf-8  -*-
#@File:test-1106.py
#@Time:2021/11/1621:37
#@site:
#@Software:PyCharm
#@Author:sfz

#a=['ss','ss','ww']
#列表的增删改查
#增加
# a.append('pp')
# print(a)
#插入 列表用insert
# a.insert(2,10)
# b=['a','ee','ww']
# a.extend(b)
# print(a)
# del a[2]
# print(a)
#算法  倒叙排列  思路 第一项与最后一项索引的值交换 依次进行下去
 # alist = [5,8,6,9,3,4,8,9,5,1,4,2]
 # alist1=[]
 # for i in range(len(alist)-1):
 #     alist1[i]=alist[len(alist)-1-i]
 #     print(alist1)
# alist = [5,8,6,9,3,4,8,9,5,1,4,2]#定义一个列表
# list_len = len(alist)#获取列表的长度
# print(list_len)
# l_len = list_len//2#取整  6
# for i in range(l_len): #i的值  0-5,range函数，默认从0开始
#     alist[i],alist[list_len-1-i] = alist[list_len-1-i], alist[i]
#     #alist[i]=alist[list_len-1-i]    alist[list_len-1-i]=alist[i]
#  #第一次循环   alist[0]=2        alist[11]=5      alist=[2,8,6,9,3,4,8,9,5,1,4,5]
#  #第二次循环   alist[1]=4        alist[10]=8      alist=[2,4,6,9,3,4,8,9,5,1,8,5]
#  #……
# print(alist)
# print (alist)
# alist.reverse()
# print(alist)

#冒泡排序  实现的是从小到大的顺序排序
# 实现原理  那索引的第一个值跟后面所有的元组做一一比较
# 如果当前索引的值大于后面的值 两个做交换 直到列表遍历完成才会结束本次循环
# alist = [5,8,1,2]#定义一个列表
# le=len(alist)#4
# for i in range(le-1):#0-3
#     for j in range(i,le):#
#         if alist[i]>alist[j]:
#             alist[i],alist[j]=alist[j],alist[i]
#
#
#     print(alist)


#思考题
serverLog = '''
2019-02-18 20:12:27	82期	liuyang	90
2019-02-18 00:15:00	84期	yangxue	73
2019-02-18 11:12:27	81期	zhufeng	69
2019-02-18 22:10:07	81期	liuli	100
2019-02-18 23:13:44	83期	yangzheng	93
'''
alist=[]#用于存放数据  [[期数，分数，人数],[期数，分数，人数]……]
serverLog_list01=serverLog.split('\n')[1:-1]
for i in range(len(serverLog_list01)):
    qishu=serverLog_list01[i].split('\t')[1]
    score=int(serverLog_list01[i].split('\t')[3])
    #list03 = serverLog_list01[i].split('\t')[2]
    flag=False
    for j in alist:
        #print(i)
        if j[0]==qishu:
            j[1]+=score
            j[2]+=1
            flag=True
    if flag==False:
         alist.append([qishu,score,1])
print(alist)
#print(serverLog_list01)

print('ok')