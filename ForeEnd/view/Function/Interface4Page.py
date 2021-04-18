# @Time : 2021/1/20 11:30
# @Author : XX
# @File : Interface4Page.py
# @Project : QFrame
# @Software : PyCharm
from BackEnd.controller.TestController import TestController
from ForeEnd.model.form.function import Ui_Function
from Tool.InitPage import InitPage


class Interface4Page(InitPage):
    def __init__(self, ui: Ui_Function):
        self.ui = ui
        self.testController = TestController()
        self.initParamter()  ##初始化参数
        self.registerEvent()##注册页面内事件
    ##初始化页面内所有参数
    def initParamter(self):
        pass
    ##注册页面内事件绑定
    def registerEvent(self):
        pass