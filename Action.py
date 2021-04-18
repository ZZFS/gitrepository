# @Time : 2021/1/12 12:13
# @Author : XX
# @File : Action.py
# @Project : QFrame
# @Software : PyCharm
from PySide2 import QtWidgets, QtGui
from PySide2.QtWidgets import QApplication

from ForeEnd.window.MainWindow import Main1

if __name__ == '__main__':
    app = QApplication([])
    mainw = Main1()
    mainw.showFullScreen()
    QtWidgets.QShortcut(QtGui.QKeySequence('Esc', ), mainw, mainw.close)
    app.exec_()
