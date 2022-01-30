from sql课设.initialUI.register import register
from mysql import rdsSql
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class registerWin(QWidget,register):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.rds = rdsSql(host="localhost", user="root", password="123456", database="mytest")
        self.submit.clicked.connect(self.submitInfo)

    def submitInfo(self):
        account = self.accountEdit.text()
        name = self.nameEdit.text()
        email = self.emailEdit.text()
        card = self.cardNumEdit.text()
        phone = self.phoneEdit.text()
        password = self.passwordEdit.text()
        if (account != "" and name != "" and email != "" and card != "" and phone != "" and password != ""):
            if (self.rds.insert(
                    "insert into client(c_id,c_name,c_mail,c_id_card,c_phone,c_password)values(%s,%s,%s,%s,%s,%s)",
                    (account, name, email, card, phone, password))):
                mesBox = QMessageBox()
                mesBox.information(self, "提示", "注册成功", buttons=QMessageBox.Ok)
                mesBox.show()
            else:
                mesBox = QMessageBox()
                mesBox.warning(self, "提示", "信息未填写完整", buttons=QMessageBox.Ok)
                mesBox.show()
