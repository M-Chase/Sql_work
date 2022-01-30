from mysql import rdsSql
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sql课设.initialUI.main import main
from sql课设.manageWin import manageWin
from sql课设.showWin import showWin
from sql课设.updateWin import updateWin

class mainWin(QWidget,main):
    def __init__(self,account):
        super().__init__()
        self.setupUi(self)
        self.checkBtn.clicked.connect(self.checkInfo)
        self.manageBtn.clicked.connect(self.toManageWin)
        self.showBtn.clicked.connect(self.toShow)
        self.updateBtn.clicked.connect(self.updateInfo)
        self.account=account
        self.rds = rdsSql(host="localhost", user="root", password="123456", database="mytest")

    def checkInfo(self):
        self.getproperty()
        self.getbankCard()
        self.getfinances()
        self.getfund()
        self.getinsurance()

    def getproperty(self):
        sql = "select * from property where pro_c_id=%s"
        self.property = self.rds.search(sql, data=self.account)
        rowNum = len(self.property)  # 获取查询到的行数
        if rowNum!=0:
            columnNum = len(self.property[0])  # 获取查询到的列数
            self.productTable.setRowCount(rowNum)  # 设置表格行数
            self.productTable.setColumnCount(columnNum)
            self.productTable.setHorizontalHeaderLabels(
                ["pro_id", "pro_c_id", "pro_pif_id", "pro_type", "pro_status", "pro_quantity", "pro_income",
                 "pro_purchase_time"])

            for i, da in enumerate(self.property):
                for j in range(columnNum):
                    self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                    self.productTable.setItem(i, j, self.itemContent)
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "您暂时没有购买任何产品", buttons=QMessageBox.Ok)
            mesBox.show()

    def getfinances(self):
        sql = "select * from finances_product where p_id in (select pro_pif_id from property where pro_c_id=%s)"
        self.finances = self.rds.search(sql, data=self.account)
        rowNum = len(self.finances)  # 获取查询到的行数
        if rowNum != 0:
            columnNum = len(self.finances[0])  # 获取查询到的列数
            self.financesTable.setRowCount(rowNum)  # 设置表格行数
            self.financesTable.setColumnCount(columnNum)
            self.financesTable.setHorizontalHeaderLabels(
                ["p_name", "p_id", "p_description", "p_amount", "p_year"])

            for i, da in enumerate(self.finances):
                for j in range(columnNum):
                    self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                    self.financesTable.setItem(i, j, self.itemContent)
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "您暂时没有理财产品", buttons=QMessageBox.Ok)
            mesBox.show()
    def getinsurance(self):
        sql = "select * from insurance where i_id in (select pro_pif_id from property where pro_c_id=%s)"
        self.insurance = self.rds.search(sql, data=self.account)
        rowNum = len(self.insurance)  # 获取查询到的行数
        if rowNum != 0:
            columnNum = len(self.insurance[0])  # 获取查询到的列数
            self.insuranceTable.setRowCount(rowNum)  # 设置表格行数
            self.insuranceTable.setColumnCount(columnNum)
            self.insuranceTable.setHorizontalHeaderLabels(
                ["p_name", "p_id", "p_description", "p_amount", "p_year"])

            for i, da in enumerate(self.insurance):
                for j in range(columnNum):
                    self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                    self.insuranceTable.setItem(i, j, self.itemContent)
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "您暂时没有保险", buttons=QMessageBox.Ok)
            mesBox.show()
    def getfund(self):
        sql = "select * from fund where f_id in(select pro_pif_id from property where pro_c_id=%s)"
        self.fund = self.rds.search(sql, data=self.account)
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
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "您暂时没有基金", buttons=QMessageBox.Ok)
            mesBox.show()

    def getbankCard(self):
        sql = "select * from bank_card where b_c_id=%s"
        self.bankCard = self.rds.search(sql, data=self.account)
        rowNum = len(self.bankCard)  # 获取查询到的行数
        if rowNum != 0:
            columnNum = len(self.bankCard[0])  # 获取查询到的列数
            self.cardTable.setRowCount(rowNum)  # 设置表格行数
            self.cardTable.setColumnCount(columnNum)
            self.cardTable.setHorizontalHeaderLabels(
                ["b_number","b_type","b_c_id"])

            for i, da in enumerate(self.bankCard):
                for j in range(columnNum):
                    self.itemContent = QTableWidgetItem(('%s') % (da[j]))
                    self.cardTable.setItem(i, j, self.itemContent)
        else:
            mesBox = QMessageBox()
            mesBox.warning(self, "提示", "您暂时没有银行卡", buttons=QMessageBox.Ok)
            mesBox.show()


    def toManageWin(self):
        self.manageWin=manageWin(self.account)
        self.manageWin.show()

    def toShow(self):
        self.showWin=showWin()
        self.showWin.show()
        pass
    def updateInfo(self):
        self.updateWin=updateWin(self.account)
        self.updateWin.show()

