#-*-  coding:utf-8  -*-
#@File:pachong获取全部正文.py
#@Time:2021/11/2018:48
#@site:
#@Software:PyCharm
#@Author:sfz
#网络爬虫，requests
import requests
import re
import os
import xlrd,xlwt
url='http://www.qxtxt.com/'#需要进行爬虫的网址
#url2=re.findall('http://www.qxtxt.com/(.*?)/',url)[0]#http://www.qxtxt.com/longzu5daowangzhedeguilai/52541.html
req=requests.get(url)#获取网页内容https://www.xs4.cc/0_3/' #需要
#req.encoding="gbk"#将编码转为jbk模式
# print(req.text)
book_name=re.findall('<h1>(.*?)</h1>',req.text)[0]#找到书名
#print(book_name)
#目录


mulu=re.findall('html"(.*?)>(.*?)</a>',req.text,re.S)#获取所有章节目录

# for one in mulu:
#     print(list(one)[-1])

wangzhi=re.findall(f'<a href="/(.*?).html"',req.text,re.S)#获取所有章节目录的网址
#print(wangzhi)

dict1={}#新建一个字典，等下用于存放目录和网址
for i in range(31,len(mulu)):
    mulu[i]=list(mulu[i])[-1]
    dict1[mulu[i]]=f'{url}{wangzhi[i]}.html'#将目录和网址存放在字典中
#print(dict1)
# data=xlrd.open_workbook(f'd:/{book_name}.xls')#读取一个excel文件
# sheet1=data.sheets()[0]#读取文件的第一个sheet
# mulu1=[]
# for i in range(1,sheet1.nrows):#nrows返回excel中的有效行数
#     #print(sheet1.cell_value(i,0),sheet1.cell_value(i,1))

if os.path.exists(f'd:/{book_name}'):#如果目录已经存在，则不新建文件夹
    pass
else:
    os.mkdir(f'd:/{book_name}')#如果目录不存在，则创建以书名的目录
count=0
for k, v in dict1.items():
    if count>=3:
        break
    else:
        zhengwen=requests.get(v)#获取正文页面的所有html内容
        zhengwen.encoding='utf-8'#解决乱码问题
        neirong=re.findall('<p>(.*?)</p>',zhengwen.text,re.S)[0]
        neirong=neirong.replace('<p>','').replace('&rdquo;','').replace('/','').replace('&ldquo;','').replace('&lt;','').replace('&nbsp','').replace('&mdash;','').replace('&amp;ldquo;','').replace('<br >','').replace('&hellip;','').replace('<br />','').replace('p&gt;','')#去掉不需要的字符
        with open(f'd:/{book_name}/{k}.txt','w+') as file1:
            file1.write(neirong)
        count+=1
#获取全部正文，自己编写的。
