# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main1(object):
    def setupUi(self, Main1):
        if not Main1.objectName():
            Main1.setObjectName(u"Main1")
        Main1.resize(1244, 868)
        Main1.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(Main1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.main01_widget = QWidget(Main1)
        self.main01_widget.setObjectName(u"main01_widget")
        self.main01_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.main01_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(17, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_2.setStretch(0, 15)
        self.horizontalLayout_2.setStretch(1, 5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.main01_pushButton = QPushButton(self.main01_widget)
        self.main01_pushButton.setObjectName(u"main01_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main01_pushButton.sizePolicy().hasHeightForWidth())
        self.main01_pushButton.setSizePolicy(sizePolicy)
        self.main01_pushButton.setMinimumSize(QSize(0, 100))
        self.main01_pushButton.setMaximumSize(QSize(200, 100))
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.main01_pushButton.setFont(font)
        self.main01_pushButton.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(85, 255, 255);\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255, 0, 0);\n"
"font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";}")

        self.horizontalLayout_3.addWidget(self.main01_pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.main01_pushButton_3 = QPushButton(self.main01_widget)
        self.main01_pushButton_3.setObjectName(u"main01_pushButton_3")
        sizePolicy.setHeightForWidth(self.main01_pushButton_3.sizePolicy().hasHeightForWidth())
        self.main01_pushButton_3.setSizePolicy(sizePolicy)
        self.main01_pushButton_3.setMinimumSize(QSize(0, 100))
        self.main01_pushButton_3.setMaximumSize(QSize(200, 100))
        self.main01_pushButton_3.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(85, 255, 255);\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255, 0, 0);\n"
"font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";}")

        self.horizontalLayout_3.addWidget(self.main01_pushButton_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.pushButton = QPushButton(self.main01_widget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(200, 100))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border-radius:20px;\n"
"font: 12pt \"\u5fae\u8f6f\u96c5\u9ed1\";\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(85, 255, 255);\n"
"	background-color: rgb(85, 85, 0);\n"
"}\n"
"QPushButton:hover{\n"
"border:2px solid rgb(255, 0, 0);\n"
"font: 15pt \"\u5fae\u8f6f\u96c5\u9ed1\";}")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(3, 3)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.main01_widget)


        self.retranslateUi(Main1)

        QMetaObject.connectSlotsByName(Main1)
    # setupUi

    def retranslateUi(self, Main1):
        Main1.setWindowTitle(QCoreApplication.translate("Main1", u"Form", None))
        self.main01_pushButton.setText(QCoreApplication.translate("Main1", u"\u754c\u97621\u30012\u30013", None))
        self.main01_pushButton_3.setText(QCoreApplication.translate("Main1", u"\u754c\u97624", None))
        self.pushButton.setText(QCoreApplication.translate("Main1", u"\u9000\u51fa\u7cfb\u7edf", None))
    # retranslateUi

