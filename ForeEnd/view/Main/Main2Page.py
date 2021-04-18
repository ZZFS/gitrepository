# @Time : 2021/1/20 11:30
# @Author : XX
# @File : Interface1Page.py
# @Project : QFrame
# @Software : PyCharm
from ForeEnd.model.form.main2 import Ui_Main2
from Tool.InitPage import InitPage


class Main2Page(InitPage):
    def __init__(self, ui: Ui_Main2):
        self.ui = ui
        self.initParamter()##初始化参数
        self.registerEvent()##注册页面内事件
    #初始化页面内所有参数
    def initParamter(self):
        pass
    ##注册页面内事件绑定
    def registerEvent(self):
        pass