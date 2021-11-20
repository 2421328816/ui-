#-*-  coding:utf-8  -*-
#@File:爬虫.py
#@Time:2021/11/1921:37
#@site:
#@Software:PyCharm
#@Author:sfz
#看着视频敲一遍
#网络爬虫，requests
import requests
import re
import xlrd,xlwt
url='https://www.xs4.cc/0_3/'#需要进行爬虫的网址
url2=re.findall('https://www.xs4.cc/(.*?)/',url)[0]
req=requests.get(url)#获取网页内容https://www.xs4.cc/0_3/' #需要
req.encoding='gbk'#将编码转为jbk模式
# print(req.text)
book_name=re.findall('<h1(.*?)/h1>',req.text)[0]#找到书名
#目录
mulu=re.findall('html">(.*?)</a>',req.text,re.S)#获取所有章节目录
wangzhi=re.findall(f'<a href="/{url2}/(.*?).html">',req.text,re.S)#获取所有章节目录的网址

dict1={}#新建一个字典，等下用于存放目录和网址
for i in range(9,len(mulu)):
    dict1[mulu[i]]=f'{url}{wangzhi[i]}.html'#将目录和网址存放在字典中
#将目录和网址存放在excel中
excel1=xlwt.workbook()#实例化一个excel
worksheet=excel1.add_sheet(f'{book_name}')#新建一个sheet
worksheet.write(0,0,'目录')#行列内容
worksheet.write(0,1,'内容')#行列内容
row=1
for k,v in dict1.items():#遍历字典中的键和值
    worksheet.write(row,0,k)#将目录写道excel中
    worksheet.write(row,1,v)#将网址写道excel中
    row+=1
excel1.save(f'd:/{book_name}.xls')
