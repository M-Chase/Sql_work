from mysql import rdsSql
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sql课设.initialUI.update import update


class updateWin(QWidget,update):
    def __init__(self,account):
        super().__init__()
        self.setupUi(self)
        self.rds = rdsSql(host="localhost", user="root", password="123456", database="mytest")
        self.submit.clicked.connect(self.submitInfo)
        self.accountNum=account
        sql = "select * from client where c_id=%s"
        list = self.rds.search(sql, data=self.accountNum)
        self.old_account.setText(str(list[0][0]))
        self.old_name.setText(str(list[0][1]))
        self.old_email.setText(str(list[0][2]))
        self.old_cardNum.setText(str(list[0][3]))
        self.old_phone.setText(str(list[0][4]))
        self.old_password.setText(str(list[0][5]))

    def submitInfo(self):


        account=str(self.new_account.text())
        name=str(self.new_name.text())
        email=str(self.new_email.text())
        cardNum=str(self.new_cardNum.text())
        phone=str(self.new_phone.text())
        password=str(self.new_password.text())
        sql="update client set c_id=%s,c_name=%s,c_mail=%s,c_id_card=%s,c_phone=%s,c_password=%s where c_id=%s"
        data=(account,name,email,cardNum,phone,password,str(self.old_account.text()))
        isOK=self.rds.update(sql,data)
        if(isOK):
            mesBox = QMessageBox()
            mesBox.information(self, "提示", "更新成功", buttons=QMessageBox.Ok)
            mesBox.show()
