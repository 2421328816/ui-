#-*-  coding:utf-8  -*-
#@File:pachong.py
#@Time:2021/11/2012:53
#@site:
#@Software:PyCharm
#@Author:sfz
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
#将目录和网址存放在excel中
excel1=xlwt.Workbook()#实例化一个excel
worksheet=excel1.add_sheet(f'{book_name}')#新建一个sheet
worksheet.write(0,0,'目录')#行列内容
worksheet.write(0,1,'内容')#行列内容
row=1
for k,v in dict1.items():#遍历字典中的键和值
    worksheet.write(row,0,k)#将目录写道excel中
    worksheet.write(row,1,v)#将网址写道excel中
    row+=1
excel1.save(f'd:/{book_name}.xls')
#思考题：获取全部正文
#读取excel
data=xlrd.open_workbook(f'd:/{book_name}.xls')#读取一个excel文件
sheet1=data.sheets()[0]#读取文件的第一个sheet
for i in range(1,sheet1.nrows):#nrows返回excel中的有效行数
    print(sheet1.cell_value(i,0),sheet1.cell_value(i,1))