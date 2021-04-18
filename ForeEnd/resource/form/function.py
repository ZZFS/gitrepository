# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'function.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Function(object):
    def setupUi(self, Function):
        if not Function.objectName():
            Function.setObjectName(u"Function")
        Function.resize(1043, 632)
        Function.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"Arial Black")
        Function.setFont(font)
        self.verticalLayout_28 = QVBoxLayout(Function)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.hand = QStackedWidget(Function)
        self.hand.setObjectName(u"hand")
        self.hand.setStyleSheet(u"background-color: rgb(68, 187, 116);\n"
"")
        self.hand_smart1 = QWidget()
        self.hand_smart1.setObjectName(u"hand_smart1")
        self.verticalLayout_2 = QVBoxLayout(self.hand_smart1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.hand_horizontalLayout1 = QHBoxLayout()
        self.hand_horizontalLayout1.setObjectName(u"hand_horizontalLayout1")
        self.main_Button1 = QPushButton(self.hand_smart1)
        self.main_Button1.setObjectName(u"main_Button1")
        font1 = QFont()
        font1.setPointSize(15)
        self.main_Button1.setFont(font1)
        self.main_Button1.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout1.addWidget(self.main_Button1)

        self.smart1_Button1 = QPushButton(self.hand_smart1)
        self.smart1_Button1.setObjectName(u"smart1_Button1")
        font2 = QFont()
        font2.setPointSize(16)
        self.smart1_Button1.setFont(font2)
        self.smart1_Button1.setStyleSheet(u"QPushButton{border:none;color:Black;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout1.addWidget(self.smart1_Button1)

        self.smart2_Button1 = QPushButton(self.hand_smart1)
        self.smart2_Button1.setObjectName(u"smart2_Button1")
        self.smart2_Button1.setFont(font1)
        self.smart2_Button1.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout1.addWidget(self.smart2_Button1)

        self.expert_Button1 = QPushButton(self.hand_smart1)
        self.expert_Button1.setObjectName(u"expert_Button1")
        self.expert_Button1.setFont(font1)
        self.expert_Button1.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout1.addWidget(self.expert_Button1)

        self.wood_Button1 = QPushButton(self.hand_smart1)
        self.wood_Button1.setObjectName(u"wood_Button1")
        self.wood_Button1.setFont(font1)
        self.wood_Button1.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout1.addWidget(self.wood_Button1)

        self.hand_horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hand_horizontalLayout1.addItem(self.hand_horizontalSpacer1)

        self.hand_horizontalLayout1.setStretch(0, 1)
        self.hand_horizontalLayout1.setStretch(1, 1)
        self.hand_horizontalLayout1.setStretch(2, 1)
        self.hand_horizontalLayout1.setStretch(3, 1)
        self.hand_horizontalLayout1.setStretch(4, 1)
        self.hand_horizontalLayout1.setStretch(5, 2)

        self.verticalLayout_2.addLayout(self.hand_horizontalLayout1)

        self.hand.addWidget(self.hand_smart1)
        self.hand_smart2 = QWidget()
        self.hand_smart2.setObjectName(u"hand_smart2")
        self.verticalLayout_3 = QVBoxLayout(self.hand_smart2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.hand_horizontalLayout2 = QHBoxLayout()
        self.hand_horizontalLayout2.setObjectName(u"hand_horizontalLayout2")
        self.main_Button2 = QPushButton(self.hand_smart2)
        self.main_Button2.setObjectName(u"main_Button2")
        self.main_Button2.setFont(font1)
        self.main_Button2.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout2.addWidget(self.main_Button2)

        self.smart1_Button2 = QPushButton(self.hand_smart2)
        self.smart1_Button2.setObjectName(u"smart1_Button2")
        self.smart1_Button2.setFont(font1)
        self.smart1_Button2.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout2.addWidget(self.smart1_Button2)

        self.smart2_Button2 = QPushButton(self.hand_smart2)
        self.smart2_Button2.setObjectName(u"smart2_Button2")
        self.smart2_Button2.setFont(font2)
        self.smart2_Button2.setStyleSheet(u"QPushButton{border:none;color:Black;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout2.addWidget(self.smart2_Button2)

        self.expert_Button2 = QPushButton(self.hand_smart2)
        self.expert_Button2.setObjectName(u"expert_Button2")
        self.expert_Button2.setFont(font1)
        self.expert_Button2.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout2.addWidget(self.expert_Button2)

        self.wood_Button2 = QPushButton(self.hand_smart2)
        self.wood_Button2.setObjectName(u"wood_Button2")
        self.wood_Button2.setFont(font1)
        self.wood_Button2.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout2.addWidget(self.wood_Button2)

        self.hand_horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hand_horizontalLayout2.addItem(self.hand_horizontalSpacer2)

        self.hand_horizontalLayout2.setStretch(0, 1)
        self.hand_horizontalLayout2.setStretch(1, 1)
        self.hand_horizontalLayout2.setStretch(2, 1)
        self.hand_horizontalLayout2.setStretch(3, 1)
        self.hand_horizontalLayout2.setStretch(4, 1)
        self.hand_horizontalLayout2.setStretch(5, 2)

        self.verticalLayout_3.addLayout(self.hand_horizontalLayout2)

        self.hand.addWidget(self.hand_smart2)
        self.hand_expert = QWidget()
        self.hand_expert.setObjectName(u"hand_expert")
        self.verticalLayout_4 = QVBoxLayout(self.hand_expert)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.hand_horizontalLayout3 = QHBoxLayout()
        self.hand_horizontalLayout3.setObjectName(u"hand_horizontalLayout3")
        self.main_Button3 = QPushButton(self.hand_expert)
        self.main_Button3.setObjectName(u"main_Button3")
        self.main_Button3.setFont(font1)
        self.main_Button3.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout3.addWidget(self.main_Button3)

        self.smart1_Button3 = QPushButton(self.hand_expert)
        self.smart1_Button3.setObjectName(u"smart1_Button3")
        self.smart1_Button3.setFont(font1)
        self.smart1_Button3.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout3.addWidget(self.smart1_Button3)

        self.smart2_Button3 = QPushButton(self.hand_expert)
        self.smart2_Button3.setObjectName(u"smart2_Button3")
        self.smart2_Button3.setFont(font1)
        self.smart2_Button3.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout3.addWidget(self.smart2_Button3)

        self.expert_Button3 = QPushButton(self.hand_expert)
        self.expert_Button3.setObjectName(u"expert_Button3")
        self.expert_Button3.setFont(font2)
        self.expert_Button3.setStyleSheet(u"QPushButton{border:none;color:Black;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout3.addWidget(self.expert_Button3)

        self.wood_Button3 = QPushButton(self.hand_expert)
        self.wood_Button3.setObjectName(u"wood_Button3")
        self.wood_Button3.setFont(font1)
        self.wood_Button3.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout3.addWidget(self.wood_Button3)

        self.hand_horizontalSpacer3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hand_horizontalLayout3.addItem(self.hand_horizontalSpacer3)

        self.hand_horizontalLayout3.setStretch(0, 1)
        self.hand_horizontalLayout3.setStretch(1, 1)
        self.hand_horizontalLayout3.setStretch(2, 1)
        self.hand_horizontalLayout3.setStretch(3, 1)
        self.hand_horizontalLayout3.setStretch(4, 1)
        self.hand_horizontalLayout3.setStretch(5, 2)

        self.verticalLayout_4.addLayout(self.hand_horizontalLayout3)

        self.hand.addWidget(self.hand_expert)
        self.hand_wood = QWidget()
        self.hand_wood.setObjectName(u"hand_wood")
        self.verticalLayout = QVBoxLayout(self.hand_wood)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hand_horizontalLayout4 = QHBoxLayout()
        self.hand_horizontalLayout4.setObjectName(u"hand_horizontalLayout4")
        self.main_Button4 = QPushButton(self.hand_wood)
        self.main_Button4.setObjectName(u"main_Button4")
        self.main_Button4.setFont(font1)
        self.main_Button4.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout4.addWidget(self.main_Button4)

        self.smart1_Button4 = QPushButton(self.hand_wood)
        self.smart1_Button4.setObjectName(u"smart1_Button4")
        self.smart1_Button4.setFont(font1)
        self.smart1_Button4.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout4.addWidget(self.smart1_Button4)

        self.smart2_Button4 = QPushButton(self.hand_wood)
        self.smart2_Button4.setObjectName(u"smart2_Button4")
        self.smart2_Button4.setFont(font1)
        self.smart2_Button4.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout4.addWidget(self.smart2_Button4)

        self.expert_Button4 = QPushButton(self.hand_wood)
        self.expert_Button4.setObjectName(u"expert_Button4")
        self.expert_Button4.setFont(font1)
        self.expert_Button4.setStyleSheet(u"QPushButton{border:none;color:White;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout4.addWidget(self.expert_Button4)

        self.wood_Button4 = QPushButton(self.hand_wood)
        self.wood_Button4.setObjectName(u"wood_Button4")
        self.wood_Button4.setFont(font2)
        self.wood_Button4.setStyleSheet(u"QPushButton{border:none;color:Black;}\n"
"QPushButton:hover{background-color: rgb(118, 186, 161);}\n"
"QPushButton:checked{background-color:rgb(255, 255, 255);color:Black;}")

        self.hand_horizontalLayout4.addWidget(self.wood_Button4)

        self.hand_horizontalSpacer4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.hand_horizontalLayout4.addItem(self.hand_horizontalSpacer4)

        self.hand_horizontalLayout4.setStretch(0, 1)
        self.hand_horizontalLayout4.setStretch(1, 1)
        self.hand_horizontalLayout4.setStretch(2, 1)
        self.hand_horizontalLayout4.setStretch(3, 1)
        self.hand_horizontalLayout4.setStretch(4, 1)
        self.hand_horizontalLayout4.setStretch(5, 2)

        self.verticalLayout.addLayout(self.hand_horizontalLayout4)

        self.hand.addWidget(self.hand_wood)

        self.verticalLayout_28.addWidget(self.hand)

        self.down = QStackedWidget(Function)
        self.down.setObjectName(u"down")
        self.down.setStyleSheet(u"")
        self.smart1_page = QWidget()
        self.smart1_page.setObjectName(u"smart1_page")
        self.horizontalLayout_21 = QHBoxLayout(self.smart1_page)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label = QLabel(self.smart1_page)
        self.label.setObjectName(u"label")

        self.horizontalLayout_21.addWidget(self.label)

        self.down.addWidget(self.smart1_page)
        self.smart2_page = QWidget()
        self.smart2_page.setObjectName(u"smart2_page")
        self.verticalLayout_68 = QVBoxLayout(self.smart2_page)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_2 = QLabel(self.smart2_page)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_68.addWidget(self.label_2)

        self.down.addWidget(self.smart2_page)
        self.expert_page = QWidget()
        self.expert_page.setObjectName(u"expert_page")
        self.verticalLayout_27 = QVBoxLayout(self.expert_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_3 = QLabel(self.expert_page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_27.addWidget(self.label_3)

        self.down.addWidget(self.expert_page)
        self.wood_page = QWidget()
        self.wood_page.setObjectName(u"wood_page")
        self.horizontalLayout_25 = QHBoxLayout(self.wood_page)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_4 = QLabel(self.wood_page)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_25.addWidget(self.label_4)

        self.down.addWidget(self.wood_page)

        self.verticalLayout_28.addWidget(self.down)


        self.retranslateUi(Function)

        self.hand.setCurrentIndex(3)
        self.down.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Function)
    # setupUi

    def retranslateUi(self, Function):
        Function.setWindowTitle(QCoreApplication.translate("Function", u"Form", None))
        self.main_Button1.setText(QCoreApplication.translate("Function", u"\u4e3b\u754c\u9762", None))
        self.smart1_Button1.setText(QCoreApplication.translate("Function", u"  \u754c\u97621  ", None))
        self.smart2_Button1.setText(QCoreApplication.translate("Function", u"\u754c\u97622  ", None))
        self.expert_Button1.setText(QCoreApplication.translate("Function", u"\u754c\u97623", None))
        self.wood_Button1.setText(QCoreApplication.translate("Function", u"\u754c\u97624", None))
        self.main_Button2.setText(QCoreApplication.translate("Function", u"\u4e3b\u754c\u9762", None))
        self.smart1_Button2.setText(QCoreApplication.translate("Function", u"\u754c\u97621  ", None))
        self.smart2_Button2.setText(QCoreApplication.translate("Function", u"\u754c\u97622  ", None))
        self.expert_Button2.setText(QCoreApplication.translate("Function", u"\u754c\u97623", None))
        self.wood_Button2.setText(QCoreApplication.translate("Function", u"\u754c\u97624", None))
        self.main_Button3.setText(QCoreApplication.translate("Function", u"\u4e3b\u754c\u9762", None))
        self.smart1_Button3.setText(QCoreApplication.translate("Function", u"\u754c\u97621  ", None))
        self.smart2_Button3.setText(QCoreApplication.translate("Function", u"\u754c\u97622  ", None))
        self.expert_Button3.setText(QCoreApplication.translate("Function", u"\u754c\u97623", None))
        self.wood_Button3.setText(QCoreApplication.translate("Function", u"\u754c\u97624", None))
        self.main_Button4.setText(QCoreApplication.translate("Function", u"\u4e3b\u754c\u9762", None))
        self.smart1_Button4.setText(QCoreApplication.translate("Function", u"\u754c\u97621", None))
        self.smart2_Button4.setText(QCoreApplication.translate("Function", u"\u754c\u97622", None))
        self.expert_Button4.setText(QCoreApplication.translate("Function", u"\u754c\u97623", None))
        self.wood_Button4.setText(QCoreApplication.translate("Function", u"\u754c\u97624", None))
        self.label.setText(QCoreApplication.translate("Function", u"\u754c\u97621", None))
        self.label_2.setText(QCoreApplication.translate("Function", u"\u754c\u97622", None))
        self.label_3.setText(QCoreApplication.translate("Function", u"\u754c\u97623", None))
        self.label_4.setText(QCoreApplication.translate("Function", u"\u754c\u97624", None))
    # retranslateUi

