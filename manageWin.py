import datetime

from mysql import rdsSql
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sql课设.initialUI.manage import manage
class manageWin(QWidget,manage):
    def __init__(self,account):
        super().__init__()
        self.setupUi(self)
        self.cardBtn.clicked.connect(self.addCard)
        self.financeBtn.clicked.connect(self.addFinance)
        self.fundBtn.clicked.connect(self.addFund)
        self.insuranceBtn.clicked.connect(self.addInsurance)
        self.rds = rdsSql(host="localhost", user="root", password="123456", database="mytest")
        self.getInfo()
        self.account=account

    def addCard(self):
        cardNum=self.cardEdit.text()
        cardKind=self.cardKindEdit.text()
        sql="insert into bank_card(b_number,b_type,b_c_id) values (%s,%s,%s)"
        data=(cardNum,cardKind,self.account)
        isOk=self.rds.insert(sql,data=data)
        if(isOk):
            mesBox = QMessageBox()
            mesBox.information(self, "提示", "办理银行卡成功", buttons=QMessageBox.Ok)
            mesBox.show()


    def addFinance(self):
        finance=self.financeEdit.text()
        financeNum=self.financesNum.value()
        sql = "select COUNT(*) from property"
        result = self.rds.search(sql)
        sql="insert into property(pro_id,pro_c_id,pro_pif_id,pro_type,pro_status,pro_quantity,pro_income,pro_purchase_time) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data=(result[0][0],self.account,finance,'1','可用',financeNum,2000,dt)
        # isOk=self.rds.insert(sql,data)
        if(self.rds.insert(sql,data)):
            mesBox = QMessageBox()
            mesBox.information(self, "提示", "购买理财产品成功", buttons=QMessageBox.Ok)
            mesBox.show()
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "信息填写错误", buttons=QMessageBox.Ok)
            mesBox.show()

    def addFund(self):
        fund=self.fundEdit.text()
        fundNum=self.fundNum.value()
        sql = "select COUNT(*) from property"
        result = self.rds.search(sql)
        sql = "insert into property(pro_id,pro_c_id,pro_pif_id,pro_type,pro_status,pro_quantity,pro_income,pro_purchase_time) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = (result[0][0],self.account, fund, '3', '可用', fundNum, 2000, dt)
        isOk = self.rds.insert(sql, data)
        if (isOk):
            mesBox = QMessageBox()
            mesBox.information(self, "提示", "购买基金产品成功", buttons=QMessageBox.Ok)
            mesBox.show()
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "信息填写错误", buttons=QMessageBox.Ok)
            mesBox.show()

    def addInsurance(self):
        insurance=self.insuranceEdit.text()
        insuranceNum=self.insuranceNum.value()
        sql="select COUNT(*) from property"
        result=self.rds.search(sql)
        sql = "insert into property(pro_id,pro_c_id,pro_pif_id,pro_type,pro_status,pro_quantity,pro_income,pro_purchase_time) values(%s,%s,%s,%s,%s,%s,%s,%s)"

        dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = (result[0][0],self.account, insurance, '2', '可用', insuranceNum, 2000, dt)
        isOk = self.rds.insert(sql, data)
        if (isOk):
            mesBox = QMessageBox()
            mesBox.information(self, "提示", "购买保险产品成功", buttons=QMessageBox.Ok)
            mesBox.show()
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "信息填写错误", buttons=QMessageBox.Ok)
            mesBox.show()

    def getInfo(self):
        self.getinsurance()
        self.getfund()
        self.getfinances()


    def getfinances(self):
        self.finances=self.rds.search("select * from finances_product")
        rowNum = len(self.finances)  # 获取查询到的行数
        if rowNum!=0:
            columnNum = len(self.finances[0])  # 获取查询到的列数
            self.financesTable.setRowCount(rowNum)  # 设置表格行数
            self.financesTable.setColumnCount(columnNum)
            self.financesTable.setHorizontalHeaderLabels(
                ["p_name", "p_id", "p_description", "p_amount", "p_year"])

            for i, da in enumerate(self.finances):
                for j in range(columnNum):
                    self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                    self.financesTable.setItem(i, j, self.itemContent)
    def getinsurance(self):
        self.insurance=self.rds.search("select * from insurance")
        rowNum = len(self.insurance)  # 获取查询到的行数
        if rowNum != 0:
            columnNum = len(self.insurance[0])  # 获取查询到的列数
            self.insuranceTable.setRowCount(rowNum)  # 设置表格行数
            self.insuranceTable.setColumnCount(columnNum)
            self.insuranceTable.setHorizontalHeaderLabels(
                ["i_name", "i_id", "i_amount", "i_person", "i_year","i_project"])

            for i, da in enumerate(self.insurance):
                for j in range(columnNum):
                    self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                    self.insuranceTable.setItem(i, j, self.itemContent)
    def getfund(self):
        self.fund=self.rds.search("select * from fund")
        rowNum = len(self.fund)  # 获取查询到的行数
        if rowNum != 0:
            columnNum = len(self.fund[0])  # 获取查询到的列数
            self.fundTable.setRowCount(rowNum)  # 设置表格行数
            self.fundTable.setColumnCount(columnNum)
            self.fundTable.setHorizontalHeaderLabels(
                ["f_name", "f_id", "f_type", "f_amount", "risk_level", "f_manager"])

            for i, da in enumerate(self.fund):
                for j in range(columnNum):
                    self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                    self.fundTable.setItem(i, j, self.itemContent)
