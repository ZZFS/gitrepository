# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main2(object):
    def setupUi(self, Main2):
        if not Main2.objectName():
            Main2.setObjectName(u"Main2")
        Main2.resize(784, 551)
        self.verticalLayout = QVBoxLayout(Main2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Main2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.main02_label_2 = QLabel(self.widget)
        self.main02_label_2.setObjectName(u"main02_label_2")
        self.main02_label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.main02_label_2)

        self.main02_label_3 = QLabel(self.widget)
        self.main02_label_3.setObjectName(u"main02_label_3")
        self.main02_label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.main02_label_3)

        self.main02_label_4 = QLabel(self.widget)
        self.main02_label_4.setObjectName(u"main02_label_4")
        self.main02_label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.main02_label_4)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.main02_pushButton_2 = QPushButton(self.widget)
        self.main02_pushButton_2.setObjectName(u"main02_pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main02_pushButton_2.sizePolicy().hasHeightForWidth())
        self.main02_pushButton_2.setSizePolicy(sizePolicy)
        self.main02_pushButton_2.setMinimumSize(QSize(0, 100))
        self.main02_pushButton_2.setMaximumSize(QSize(200, 100))
        self.main02_pushButton_2.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(85, 255, 255);\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255, 0, 0);\n"
"font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";}")

        self.horizontalLayout_3.addWidget(self.main02_pushButton_2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.main02_pushButton_3 = QPushButton(self.widget)
        self.main02_pushButton_3.setObjectName(u"main02_pushButton_3")
        sizePolicy.setHeightForWidth(self.main02_pushButton_3.sizePolicy().hasHeightForWidth())
        self.main02_pushButton_3.setSizePolicy(sizePolicy)
        self.main02_pushButton_3.setMaximumSize(QSize(200, 100))
        self.main02_pushButton_3.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(85, 255, 255);\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255, 0, 0);\n"
"font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";}")

        self.horizontalLayout_3.addWidget(self.main02_pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.main02_pushButton_4 = QPushButton(self.widget)
        self.main02_pushButton_4.setObjectName(u"main02_pushButton_4")
        sizePolicy.setHeightForWidth(self.main02_pushButton_4.sizePolicy().hasHeightForWidth())
        self.main02_pushButton_4.setSizePolicy(sizePolicy)
        self.main02_pushButton_4.setMaximumSize(QSize(200, 100))
        self.main02_pushButton_4.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(85, 255, 255);\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255, 0, 0);\n"
"font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";}")

        self.horizontalLayout_3.addWidget(self.main02_pushButton_4)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.main02_pushButton_1 = QPushButton(self.widget)
        self.main02_pushButton_1.setObjectName(u"main02_pushButton_1")
        sizePolicy.setHeightForWidth(self.main02_pushButton_1.sizePolicy().hasHeightForWidth())
        self.main02_pushButton_1.setSizePolicy(sizePolicy)
        self.main02_pushButton_1.setMinimumSize(QSize(0, 100))
        self.main02_pushButton_1.setMaximumSize(QSize(200, 100))
        self.main02_pushButton_1.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(85, 255, 255);\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255, 0, 0);\n"
"font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";}")

        self.horizontalLayout_3.addWidget(self.main02_pushButton_1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 10)
        self.horizontalLayout_3.setStretch(2, 2)
        self.horizontalLayout_3.setStretch(3, 10)
        self.horizontalLayout_3.setStretch(4, 2)
        self.horizontalLayout_3.setStretch(5, 10)
        self.horizontalLayout_3.setStretch(6, 2)
        self.horizontalLayout_3.setStretch(7, 10)
        self.horizontalLayout_3.setStretch(8, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Main2)

        QMetaObject.connectSlotsByName(Main2)
    # setupUi

    def retranslateUi(self, Main2):
        Main2.setWindowTitle(QCoreApplication.translate("Main2", u"Form", None))
        self.main02_label_2.setText(QCoreApplication.translate("Main2", u"<html><head/><body><p>\u661f\u671f\u65e5</p></body></html>", None))
        self.main02_label_3.setText(QCoreApplication.translate("Main2", u"<html><head/><body><p>15\uff1a33</p></body></html>", None))
        self.main02_label_4.setText(QCoreApplication.translate("Main2", u"<html><head/><body><p>2020/6/21</p></body></html>", None))
        self.main02_pushButton_2.setText(QCoreApplication.translate("Main2", u"\u754c\u97621", None))
        self.main02_pushButton_3.setText(QCoreApplication.translate("Main2", u"\u754c\u97622", None))
        self.main02_pushButton_4.setText(QCoreApplication.translate("Main2", u"\u754c\u97623", None))
        self.main02_pushButton_1.setText(QCoreApplication.translate("Main2", u"\u4e3b\u754c\u9762", None))
    # retranslateUi

