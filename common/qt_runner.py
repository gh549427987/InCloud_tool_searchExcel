# coding: utf-8
# @Time    : 2021/1/10 下午7:30
# @Author  : 蟹蟹 ！！
# @FileName: qt_runner.py
# @Software: PyCharm

from common.__init__ import *

from common.xlsop import XlsOp
from common.qt_search import Search

class Main(QMainWindow):
    """
    主要代码运行逻辑
    """

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        self.xls = object # 表格处理对象， 最终对象由 self.openfile() 生成，此处是预定义

        self.main = loadUi("QTView/main.ui", self)
        self.main.pushButton.clicked.connect(self.openfile)
        self.main.pushButton_2.clicked.connect(self.search)

    # region Main 主窗口
    def openfile(self):
        file_path = QFileDialog.getOpenFileName(self, "选择.xls表格文件", os.path.join(os.getcwd(), 'Sample'), "Excel Files ("
                                                                                                   "*.xls)")
        GV.XLS = file_path[0]

        self.xls = XlsOp()
        self.main.lineEdit.setText(file_path[0])

        self.main.tabWidget.setTabText(0, file_path[0].split('/')[-1]) # 设置tab名字


        # 设置表格行数和列数
        self.main.tableWidget.setRowCount(self.xls.ws.nrows)
        self.main.tableWidget.setColumnCount(14)

        display_data = self.xls.get_data_generator() # 生成器 对象
        self.main.tableWidget.setHorizontalHeaderLabels(next(display_data))
        # self.main.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)# 表宽度自适应

        # 填充显示数据
        for i in range(1, self.xls.ws.nrows):
            datalist = next(display_data)
            for j in range(0, 14):
                new_item = QTableWidgetItem(str(datalist[j]))
                self.main.tableWidget.setItem(i-1, j, new_item)

    # endregion

    # region search 检索窗口
    def search(self):

        my_search = Search(self)
        # 在主窗口中连接信号和槽
        my_search.mySignal.connect(self.getSignalToSearch)
        my_search.exec_()

    def getSignalToSearch(self, search_return):

        try:
            if isinstance(self.xls, XlsOp):
                search_result = self.xls.search(str(search_return[0]), int(float(search_return[1]))) # 调用搜索函数，传输key和列
        except ValueError:
            traceback.print_exc()


        tab = QWidget()
        self.main.tabWidget.addTab(tab, f"TAB {GV.TAB_COUNT}")
        GV.TAB_COUNT += 1


        tab.setObjectName(f"tab{GV.TAB_COUNT}")
        # 设置内边界
        gridLayout = QGridLayout()
        gridLayout.setObjectName(f"gridLayout-{GV.TAB_COUNT}")
        # 创建表格
        tableWidget = QTableWidget(tab)
        tableWidget.setMaximumSize(QSize(16777215, 16777215))
        tableWidget.setGridStyle(Qt.CustomDashLine)
        tableWidget.setWordWrap(True)
        tableWidget.setObjectName(f"tableWidget-{GV.TAB_COUNT}")
        tableWidget.setColumnCount(0)
        tableWidget.setRowCount(0)

        verticalLayout_2 = QVBoxLayout(tab)
        verticalLayout_2.setObjectName("verticalLayout_2")
        verticalLayout_2.addWidget(tableWidget)


        keys_1 = search_result.keys()
        # 设置最大列和行
        tableWidget.setRowCount(len(keys_1))
        max_col = 0
        for key in search_result.keys():
            max_col = len(search_result[key].keys())
        tableWidget.setColumnCount(max_col)

        # 填入搜索关键字
        key_row = 0
        key_col = 0
        for key in keys_1:
            new_item = QTableWidgetItem(key)
            tableWidget.setItem(key_row, key_col, new_item)
            # 填入搜索出来的值
            if search_result[key].keys() == 0 :
                continue
            for key_2 in search_result[key].keys():
                new_item_2 = QTableWidgetItem(str(search_result[key][key_2]))
                tableWidget.setItem(key_row, key_col+1, new_item_2)
                key_col += 1

            key_row += 1
            key_col = 0
        self.main.tabWidget.setCurrentWidget(tab)


    # endregion


def run():
    app = QApplication(sys.argv)
    w = Main()
    w.show()
    sys.exit(app.exec_())