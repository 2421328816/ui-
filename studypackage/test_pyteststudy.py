#-*-  coding:utf-8  -*-
#@File:test_pyteststudy.py
#@Time:2021/11/2015:45
#@site:
#@Software:PyCharm
#@Author:sfz
#pytest是一种自动化测试框架，他是unittest的升级版
#pytest是第三方库，需要安装使用pip install pytest

#1、文件应当以test_*.py命名，或者*_test.py
#2、类必须以Test开头，且类当中不能有__init__方法
#3、方法和函数必须以test_开头
#4、断言必须使用assert

#assert 1==2#断言1==2是否相等
#assert 200 #断言**是否为真
#assert 10 in [10,56]
# assert not True
# assert 1!=2
import pytest#加载pytest模块
class Test001:
    def setup_class(self):
        print('在类方法执行前执行')
    def teardown_method(self):
        print('最后运行的线程组')

    def test_a9(self):
        print('开始测试用例')
        assert 1==2

    def test_a10(self):
        print('开始测试用例')
        assert 2== 3
    def setup_method(self):
        print('一开始运行的线程组')
    def teardown_class(self):
        print('在类运行之后运行')
#setup_method在每个方法开始之前运行，teardown_method在每个方法运行之后运行
#teardown_class，在类中所有的方法执行之后执行
if __name__ == '__main__':
    pytest.main(['test_pyteststudy.py','-s'])
#setup_module、teardown_module模块
#setup_method、teardown_method方法
#setup_class、teardown_class类
#setup_function、teardown_function函数

