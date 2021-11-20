#-*-  coding:utf-8  -*-
#@File:正则表达式.py
#@Time:2021/11/1919:40
#@site:
#@Software:PyCharm
#@Author:sfz
import re
#正则表达式，其实就是从一段字符串提取出需要的字符串
#re.findall(参数1，参数2，参数3)，参数1，是提取的规则，参数2是从哪里提取的，参数3，
# 一般有re.I,re.S，没有特殊要求时不写
# re.findall()的返回值是一个列表
str1='abbdsabafdfdx'
#.表示匹配某个字符后面的任意一个字符
print(re.findall('ab.',str1))#没有括号则都显示
#如果用括号括起来，表示只提取到内容的本身
print(re.findall('ab(.)',str1))
#*表示b后面匹配若干个b的字符，包括0个的情况
print(re.findall('ab*',str1))
#+a表示a后面有若干个b的字符，不包括0个的情况

print(re.findall('ab+',str1))
#?表示a后面有1个b或者0个b，不包括多个
print(re.findall('ab?',str1))
#.*? A(.*?)B 提取A与B之间的字符
str3='曾经沧海难为水除却巫山不是云取次花丛懒回顾半缘修道半缘君'
print(re.findall('不是(.*?)花丛',str3))#提取中间的字符
print(re.findall('不是.*?花丛',str3))#都提取
print(re.findall('不是.*',str3))#贪婪匹配，从开始不是后面都匹配提取
print(re.findall('不是.*花丛',str3))
print(re.findall('不是(.*)花丛',str3))#提取括号里面的
print(re.findall('a.?b',str1))#提取a到b直接的值，ab也在结果里面
print(re.findall('a(.?)b',str1))#提取一个字符，包括0个字符
#\w{n}匹配字母、数字、下划线，n表示匹配连续几位
str2='dsfhdsf@$#$##%<dd9dldd'
print(re.findall('\w{3}',str2))

#\W{n}大W，匹配字母、数字、下划线以外的值
print(re.findall('\W{3}',str2))
str7='''空 山不见人 
但闻 人语响 
返景 入深林 
复照青苔上 '''
#\S（大S）匹配空字符串、\t制表符、\n换行符以外的值
print(re.findall('\S',str7))
print(re.findall('\t',str7))
print(re.findall('\n',str7))
#\d匹配数字
print(re.findall('\d',str2))

#\D匹配数字以外的值
print(re.findall('\D',str2))
#^匹配开头，$匹配结尾
list1=['sdas','sdfds','opdsfds']
for one in list1:
    #查找以sd开头的字符串
    if re.findall('^sd',one):
        print(one)
    elif re.findall('ds$',one):
        print(one)
#re.I不区分大小写
str8='helloDDGDfdfdFDFWorld'
print(re.findall('hello(.*?)World',str8,re.I))

str9='''helloDDGDf
dfdFDFWorld'''
print(re.findall('hello(.*?)World',str8,re.S))

