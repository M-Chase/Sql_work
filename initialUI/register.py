# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class register(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 473)
        self.submit = QtWidgets.QPushButton(Form)
        self.submit.setGeometry(QtCore.QRect(210, 350, 93, 28))
        self.submit.setObjectName("submit")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 60, 271, 241))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.account = QtWidgets.QLabel(self.layoutWidget)
        self.account.setObjectName("account")
        self.gridLayout.addWidget(self.account, 0, 0, 1, 1)
        self.accountEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.accountEdit.setObjectName("accountEdit")
        self.gridLayout.addWidget(self.accountEdit, 0, 1, 1, 1)
        self.name = QtWidgets.QLabel(self.layoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 1, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 1)
        self.email = QtWidgets.QLabel(self.layoutWidget)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 2, 0, 1, 1)
        self.emailEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.emailEdit.setObjectName("emailEdit")
        self.gridLayout.addWidget(self.emailEdit, 2, 1, 1, 1)
        self.cardId = QtWidgets.QLabel(self.layoutWidget)
        self.cardId.setObjectName("cardId")
        self.gridLayout.addWidget(self.cardId, 3, 0, 1, 1)
        self.cardNumEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.cardNumEdit.setObjectName("cardNumEdit")
        self.gridLayout.addWidget(self.cardNumEdit, 3, 1, 1, 1)
        self.phone = QtWidgets.QLabel(self.layoutWidget)
        self.phone.setObjectName("phone")
        self.gridLayout.addWidget(self.phone, 4, 0, 1, 1)
        self.phoneEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.phoneEdit.setObjectName("phoneEdit")
        self.gridLayout.addWidget(self.phoneEdit, 4, 1, 1, 1)
        self.password = QtWidgets.QLabel(self.layoutWidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 5, 0, 1, 1)
        self.passwordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.passwordEdit.setObjectName("passwordEdit")
        self.gridLayout.addWidget(self.passwordEdit, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "注册"))
        self.submit.setText(_translate("Form", "提交"))
        self.account.setText(_translate("Form", "账号"))
        self.name.setText(_translate("Form", "名字"))
        self.email.setText(_translate("Form", "邮箱"))
        self.cardId.setText(_translate("Form", "卡号"))
        self.phone.setText(_translate("Form", "手机"))
        self.password.setText(_translate("Form", "密码"))
