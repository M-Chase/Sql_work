import PyQt5
from sql课设.initialUI.login import login
from mysql import rdsSql
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sql课设.registerWin import registerWin
from sql课设.mainWin import mainWin
import sys
import os
# dirname = os.path.dirname(PyQt5.__file__)
# plugin_path = os.path.join(dirname, 'plugins', 'platforms')
# os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
class loginWin(QWidget,login):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.login.clicked.connect(self.judgeLogin)
        self.register_2.clicked.connect(self.toRegister)
        self.rds = rdsSql(host="localhost", user="root", password="123456", database="mytest")

    def judgeLogin(self):
        account=self.accountEdit.text()
        password=self.passwordEdit.text()
        sql="select c_id,c_password from client where c_id=%s"
        list=self.rds.search(sql,data=account)
        # print(list[0][0],list[0][1])
        if(len(list)!=0 and str(list[0][0])==account and str(list[0][1])==password):
            mesBox = QMessageBox()
            mesBox.information(self, "提示", "登录成功", buttons=QMessageBox.Ok)
            mesBox.show()
            self.mainWin=mainWin(account)
            self.mainWin.show()
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "登陆失败", buttons=QMessageBox.Ok)
            mesBox.show()

        print(list)

    def toRegister(self):
        # self.hide()
        # self.registerWidget = QWidget()
        self.register = registerWin()
        self.register.show()
        # self.register.setupUi(self.registerWidget)
        # self.registerWidget.show()

if __name__=="__main__":


    app=QApplication(sys.argv)
    # widget=QWidget()
    ui=loginWin()
    # ui.setupUi(widget)
    ui.show()
    sys.exit(app.exec_())