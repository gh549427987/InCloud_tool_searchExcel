# coding: utf-8
# @Time    : 2021/1/10 下午10:08
# @Author  : 蟹蟹 ！！
# @FileName: qt_search.py
# @Software: PyCharm

from common.__init__ import *


class Search(QDialog):

    mySignal = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super(Search, self).__init__(parent)

        self.search = loadUi("QTView/search.ui", self)
        self.search.pushButton.clicked.connect(self.go_search)

    def go_search(self):
        """

        :return: 返回检索的key和列数
        """
        search_key = self.search.textEdit.toPlainText()
        search_key = search_key.split('\n') # 转成list

        search_col = self.search.lineEdit.text() # 列数

        search_return = (search_key, search_col)

        self.mySignal.emit(search_return)

def run():
    app = QApplication(sys.argv)
    w = Search()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()

