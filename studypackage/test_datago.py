#-*-  coding:utf-8  -*-
#@File:datago.py
#@Time:2021/11/2016:58
#@site:
#@Software:PyCharm
#@Author:sfz
#数据驱动，也就是参数化
import pytest
import os
import allure#加载allure模块
# class Test2:
#     @pytest.mark.parametrize('result,real_result',([2**3,8],[3**3,28],['嘻嘻','戏ix']))#数据驱动
#     def test10(self,result,real_result):
#         assert result==real_result
@allure.feature('一级标签')#一级标签
class Test99:
    @allure.story('层级二')#二级标签
    @allure.title('层级三')#三级标签
    def test_978(self):
        assert 1==2

if __name__ == '__main__':
    pytest.main(['test_datago.py','-s','-v','--alluredir','../report'])
    os.system('allure generate ../report -o ../report/report --clean')
