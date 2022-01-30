# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'show.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class show(object):
    def setupUi(self, Form):
        Form.setObjectName("可视化界面")
        Form.resize(1095, 851)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1091, 841))
        self.tabWidget.setObjectName("tabWidget")
        self.cardTab = QtWidgets.QWidget()
        self.cardTab.setObjectName("cardTab")
        self.tabWidget.addTab(self.cardTab, "")
        self.productTab = QtWidgets.QWidget()
        self.productTab.setObjectName("productTab")
        self.tabWidget.addTab(self.productTab, "")
        self.incomeTab = QtWidgets.QWidget()
        self.incomeTab.setObjectName("incomeTab")
        self.tabWidget.addTab(self.incomeTab, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "可视化界面"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cardTab), _translate("Form", "银行卡"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.productTab), _translate("Form", "产品"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.incomeTab), _translate("Form", "收入"))

