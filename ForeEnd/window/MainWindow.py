# @Time : 2021/1/14 22:12
# @Author : XX
# @File : MainWindow.py
# @Project : QFrame
# @Software : PyCharm
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QWidget

from ForeEnd.model.form.function import Ui_Function
from ForeEnd.model.form.main1 import Ui_Main1
from ForeEnd.model.form.main2 import Ui_Main2
from ForeEnd.view.Function.Interface1Page import Interface1Page
from ForeEnd.view.Function.Interface2Page import Interface2Page
from ForeEnd.view.Function.Interface3Page import Interface3Page
from ForeEnd.view.Function.Interface4Page import Interface4Page
from ForeEnd.view.Main.Main1Page import Main1Page
from ForeEnd.view.Main.Main2Page import Main2Page


class Main1(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main1()##初始化界面
        self.ui.setupUi(self)##将自身赋值给界面
        self.registerPage()##注册界面
        self.registerEvent()##注册事件
    ##切换到当前界面
    def changeCurrentPage(self, index):
        pass
    ##注册页面
    def registerPage(self):
        self.main1Page = Main1Page(self.ui)
    ##注册页面之间切换事件
    def registerEvent(self):
        self.ui.main01_pushButton_3.clicked.connect(lambda: self.changeToFunction(3))
        self.ui.main01_pushButton.clicked.connect(self.changeToMain2)
        self.ui.pushButton.clicked.connect(self.exit)
    def changeToFunction(self,index):
        self.hide()
        self.function = Function()
        self.function.changeCurrentPage(index)
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc', ), self.function, self.function.close)
        self.function.showFullScreen()
    ##切换至主界面2
    def changeToMain2(self):
        self.hide()
        self.arithmeticChooce = Main2()
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc', ), self.arithmeticChooce, self.arithmeticChooce.close)
        self.arithmeticChooce.showFullScreen()
    def exit(self):
        self.close()
class Main2(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Main2()
        self.ui.setupUi(self)
        self.registerPage()
        self.registerEvent()
    ##切换到当前界面
    def changeCurrentPage(self, index):
        pass
    ##注册页面
    def registerPage(self):
        self.main2Page = Main2Page(self.ui)
    ##注册页面之间切换事件
    def registerEvent(self):
        self.ui.main02_pushButton_2.clicked.connect(lambda: self.changeToFunction(0))
        self.ui.main02_pushButton_1.clicked.connect(self.changeToMain1)
        self.ui.main02_pushButton_3.clicked.connect(lambda: self.changeToFunction(1))
        self.ui.main02_pushButton_4.clicked.connect(lambda: self.changeToFunction(2))
    #切换至业务功能界面
    def changeToFunction(self, index):
        self.hide()
        self.function = Function()
        self.function.changeCurrentPage(index)
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc', ), self.function, self.function.close)
        self.function.showFullScreen()
    #切换至主界面1
    def changeToMain1(self):
        self.hide()
        self.main1 = Main1()
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc', ), self.main1, self.main1.close)
        self.main1.showFullScreen()

class Function(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Function()
        self.ui.setupUi(self)
        self.registerPage()
        self.registerEvent()
    ##切换到当前界面
    def changeCurrentPage(self, index):
        self.ui.hand.setCurrentIndex(index)
        self.ui.down.setCurrentIndex(index)
    ##注册页面
    def registerPage(self):
        self.interface1Page = Interface1Page(self.ui)
        self.interface2Page = Interface2Page(self.ui)
        self.interface3Page = Interface3Page(self.ui)
        self.interface4Page = Interface4Page(self.ui)
    ##注册页面之间切换事件
    def registerEvent(self):
        self.ui.main_Button1.clicked.connect(self.changeToMain1)
        self.ui.main_Button2.clicked.connect(self.changeToMain1)
        self.ui.main_Button3.clicked.connect(self.changeToMain1)
        self.ui.main_Button4.clicked.connect(self.changeToMain1)

        self.ui.smart1_Button1.clicked.connect(self.changeToSmart1)
        self.ui.smart1_Button2.clicked.connect(self.changeToSmart1)
        self.ui.smart1_Button3.clicked.connect(self.changeToSmart1)
        self.ui.smart1_Button4.clicked.connect(self.changeToSmart1)

        self.ui.smart2_Button1.clicked.connect(self.changeToSmart2)
        self.ui.smart2_Button2.clicked.connect(self.changeToSmart2)
        self.ui.smart2_Button3.clicked.connect(self.changeToSmart2)
        self.ui.smart2_Button4.clicked.connect(self.changeToSmart2)

        self.ui.expert_Button1.clicked.connect(self.changeToExpert)
        self.ui.expert_Button2.clicked.connect(self.changeToExpert)
        self.ui.expert_Button3.clicked.connect(self.changeToExpert)
        self.ui.expert_Button4.clicked.connect(self.changeToExpert)

        self.ui.wood_Button1.clicked.connect(self.changeToWood)
        self.ui.wood_Button2.clicked.connect(self.changeToWood)
        self.ui.wood_Button3.clicked.connect(self.changeToWood)
        self.ui.wood_Button4.clicked.connect(self.changeToWood)
    #切换至主界面1
    def changeToMain1(self):
        self.hide()
        self.main1 = Main1()
        self.main1.showFullScreen()
        QtWidgets.QShortcut(QtGui.QKeySequence('Esc', ), self.main1, self.main1.close)
    #切换至智能算法界面1
    def changeToSmart1(self):
        self.ui.hand.setCurrentIndex(0)
        self.ui.down.setCurrentIndex(0)
    #切换至智能算法界面2
    def changeToSmart2(self):
        self.ui.hand.setCurrentIndex(1)
        self.ui.down.setCurrentIndex(1)
    #切换至专家辅助界面
    def changeToExpert(self):
        self.ui.hand.setCurrentIndex(2)
        self.ui.down.setCurrentIndex(2)
    #切换至木材界面
    def changeToWood(self):
        self.ui.hand.setCurrentIndex(3)
        self.ui.down.setCurrentIndex(3)