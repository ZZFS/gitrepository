# @Time : 2021/1/20 11:30
# @Author : XX
# @File : Interface1Page.py
# @Project : QFrame
# @Software : PyCharm
from ForeEnd.model.form.main1 import Ui_Main1
from Tool.InitPage import InitPage


class Main1Page(InitPage):
    def __init__(self, ui: Ui_Main1):
        self.ui = ui
        self.initParamter()##初始化参数
        self.registerEvent()##注册页面内事件
    #初始化页面内所有参数
    def initParamter(self):
        pass
    ##注册页面内事件绑定
    def registerEvent(self):
        pass