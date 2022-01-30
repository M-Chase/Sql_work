# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class login(object):
    def setupUi(self, Form):
        Form.setObjectName("登录")
        Form.resize(592, 392)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 100, 291, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.account = QtWidgets.QLabel(self.layoutWidget)
        self.account.setObjectName("account")
        self.gridLayout.addWidget(self.account, 0, 0, 1, 1)
        self.accountEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.accountEdit.setStyleSheet("background-color: rgb(0,0,0,2);\n"
"selection-background-color: rgb(255, 255, 255);\n"
"")
        self.accountEdit.setObjectName("accountEdit")
        self.gridLayout.addWidget(self.accountEdit, 0, 1, 1, 1)
        self.password = QtWidgets.QLabel(self.layoutWidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordEdit.setStyleSheet("background-color: rgb(0,0,0,2);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.passwordEdit.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.passwordEdit.setObjectName("passwordEdit")
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.passwordEdit, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 240, 195, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login = QtWidgets.QPushButton(self.layoutWidget1)
        self.login.setStyleSheet("")
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.register_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.register_2.setObjectName("register_2")
        self.horizontalLayout.addWidget(self.register_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "登录"))
        self.account.setText(_translate("Form", "账号"))
        self.password.setText(_translate("Form", "密码"))
        self.login.setText(_translate("Form", "登录"))
        self.register_2.setText(_translate("Form", "注册"))

