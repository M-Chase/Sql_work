from PyQt5.QtWebEngineWidgets import QWebEngineView
from pyecharts.charts import *
import pyecharts.options as opts
from mysql import rdsSql
from PyQt5.QtCore import*
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sql课设.initialUI.show import show

class showWin(QWidget,show):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.browser1 = QWebEngineView()
        self.browser2 = QWebEngineView()
        self.browser3 = QWebEngineView()
        self.rds = rdsSql(host="localhost", user="root", password="123456", database="mytest")
        self.showCard()
        self.showProduct()
        self.showIncom()

    def showCard(self):
        sql="select COUNT(*) from bank_card where b_type='信用卡'"
        card1=self.rds.search(sql)
        sql="select COUNT(*) from bank_card where b_type='储蓄卡'"
        card2=self.rds.search(sql)
        attr=["信用卡","储蓄卡"]
        value=[card1[0][0],card2[0][0]]
        pie=(Pie()
             .add(
            "",
            [list(z) for z in zip(attr,value)],
            label_opts=opts.LabelOpts(is_show=False, position="center"),
        )
             .render("pie.html")
        )
        self.browser1.load(QUrl("file:///pie.html"))
        layout = QFormLayout()
        layout.addWidget(self.browser1)
        self.cardTab.setLayout(layout)


    def showProduct(self):
        sql="select SUM(pro_quantity) from property where pro_type='1' and pro_pif_id='1'"
        finances_1=self.rds.search(sql)
        sql = "select SUM(pro_quantity) from property where pro_type='1' and pro_pif_id='2'"
        finances_2 = self.rds.search(sql)
        sql = "select SUM(pro_quantity) from property where pro_type='1' and pro_pif_id='3'"
        finances_3 = self.rds.search(sql)
        sql = "select SUM(pro_quantity) from property where pro_type='1' and pro_pif_id='4'"
        finances_4 = self.rds.search(sql)
        sql="select p_name from finances_product"
        financesName=self.rds.search(sql)

        sql="select SUM(pro_quantity) from property where pro_type='2' and pro_pif_id='1'"
        insurance_1=self.rds.search(sql)
        sql = "select SUM(pro_quantity) from property where pro_type='2' and pro_pif_id='2'"
        insurance_2 = self.rds.search(sql)
        sql = "select SUM(pro_quantity) from property where pro_type='2' and pro_pif_id='3'"
        insurance_3 = self.rds.search(sql)
        sql = "select SUM(pro_quantity) from property where pro_type='2' and pro_pif_id='4'"
        insurance_4 = self.rds.search(sql)
        sql="select i_name from insurance"
        insuranceName=self.rds.search(sql)

        sql="select SUM(pro_quantity) from property where pro_type='3' and pro_pif_id='1'"
        fund_1=self.rds.search(sql)
        sql = "select SUM(pro_quantity) from property where pro_type='3' and pro_pif_id='2'"
        fund_2 = self.rds.search(sql)
        sql = "select SUM(pro_quantity) from property where pro_type='3' and pro_pif_id='3'"
        fund_3 = self.rds.search(sql)
        sql="select SUM(pro_quantity) from property where pro_type='3' and pro_pif_id='4'"
        fund_4=self.rds.search(sql)
        sql="select f_name from fund"
        fundName=self.rds.search(sql)

        attr = [fundName[0][0],fundName[1][0],fundName[2][0],fundName[3][0],
                financesName[0][0],financesName[1][0],financesName[2][0],financesName[3][0],
               insuranceName[0][0],insuranceName[1][0],insuranceName[2][0],insuranceName[3][0]]
        value = [fund_1[0][0],fund_2[0][0],fund_3[0][0],fund_4[0][0],
                 finances_1[0][0],finances_2[0][0],finances_3[0][0],finances_4[0][0],
                 insurance_1[0][0],insurance_2[0][0],insurance_3[0][0],insurance_4[0][0]]
        bar=(Bar()
             .add_xaxis(attr)
             .add_yaxis("",value,label_opts=opts.LabelOpts(is_show=True))
             .set_global_opts(legend_opts=opts.LegendOpts(is_show=True),
                              datazoom_opts=opts.DataZoomOpts(is_show=True),
                              toolbox_opts=opts.ToolboxOpts(is_show=True),
                              tooltip_opts=opts.TooltipOpts(is_show=True),
                              axispointer_opts=opts.AxisPointerOpts(is_show=True))
             .render("bar.html")
             )
        # bar.add_xaxis(attr)
        # bar.add_yaxis(value,label_opts=opts.LabelOpts(is_show=False))
        # bar.render('bar.html')
        self.browser2.load(QUrl("file:///bar.html"))
        layout = QFormLayout()
        layout.addWidget(self.browser2)
        self.productTab.setLayout(layout)



    def showIncom(self):
        sql = "select SUM(pro_income) from property where pro_type='1' and pro_pif_id='1'"
        finances_1 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='1' and pro_pif_id='2'"
        finances_2 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='1' and pro_pif_id='3'"
        finances_3 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='1' and pro_pif_id='4'"
        finances_4 = self.rds.search(sql)
        sql = "select p_name from finances_product"
        financesName = self.rds.search(sql)

        sql = "select SUM(pro_income) from property where pro_type='2' and pro_pif_id='1'"
        insurance_1 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='2' and pro_pif_id='2'"
        insurance_2 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='2' and pro_pif_id='3'"
        insurance_3 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='2' and pro_pif_id='4'"
        insurance_4 = self.rds.search(sql)
        sql = "select i_name from insurance"
        insuranceName = self.rds.search(sql)

        sql = "select SUM(pro_income) from property where pro_type='3' and pro_pif_id='1'"
        fund_1 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='3' and pro_pif_id='2'"
        fund_2 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='3' and pro_pif_id='3'"
        fund_3 = self.rds.search(sql)
        sql = "select SUM(pro_income) from property where pro_type='3' and pro_pif_id='4'"
        fund_4 = self.rds.search(sql)
        sql = "select f_name from fund"
        fundName = self.rds.search(sql)

        attr = [fundName[0][0], fundName[1][0], fundName[2][0], fundName[3][0],
                financesName[0][0], financesName[1][0], financesName[2][0], financesName[3][0],
                insuranceName[0][0], insuranceName[1][0], insuranceName[2][0], insuranceName[3][0]]
        value = [fund_1[0][0], fund_2[0][0], fund_3[0][0], fund_4[0][0],
                 finances_1[0][0], finances_2[0][0], finances_3[0][0], finances_4[0][0],
                 insurance_1[0][0], insurance_2[0][0], insurance_3[0][0], insurance_4[0][0]]
        bar = (Bar()
               .add_xaxis(attr)
               .add_yaxis("",value, label_opts=opts.LabelOpts(is_show=True))
               .set_global_opts(legend_opts=opts.LegendOpts(is_show=True),
                                datazoom_opts=opts.DataZoomOpts(is_show=True),
                                toolbox_opts=opts.ToolboxOpts(is_show=True),
                                tooltip_opts=opts.TooltipOpts(is_show=True),
                                axispointer_opts=opts.AxisPointerOpts(is_show=True))
               .render("bar2.html")

               )
        # bar.add_xaxis(attr)
        # bar.add_yaxis(value, label_opts=opts.LabelOpts(is_show=False))
        # bar.render('bar2.html')
        self.browser3.load(QUrl("file:///bar2.html"))
        layout = QFormLayout()
        layout.addWidget(self.browser3)
        self.incomeTab.setLayout(layout)

