# coding: utf-8
# @Time    : 2021/1/10 下午8:28
# @Author  : 蟹蟹 ！！
# @FileName: xlsop.py
# @Software: PyCharm

from common.global_value import GV
import xlrd

class XlsOp(object):

    def __init__(self):
        self.wboook = xlrd.open_workbook(GV.XLS)
        self.ws = self.wboook.sheet_by_index(0)
        pass

    def get_data_generator(self):
        GV.XLS = r"/Users/jhua/PycharmProjects/InCloud_tool_searchExcel/Sample/sample.xls"

        for i in range(self.ws.nrows):
            data = []
            for j in range(self.ws.ncols):
                data.append(self.ws.cell_value(i,j))
            yield data

    def search(self, search_key, search_col):
        """

        :param search_key: 关键字
        :param search_col: 列
        :return:
        """
        search_result = {}
        search_key = eval(search_key)
        for key in search_key:
            search_result[key] = {}

        for key in search_key:
            count = 1
            for i in range(1, self.ws.nrows):
                for j in range(0, self.ws.ncols):
                    if key in str(self.ws.cell_value(i, j)):
                        # 返回{ "key1":{"1":"12313", "2":"231231",....}
                        search_result[key][count] = self.ws.cell_value(i, search_col-1)
                        count += 1

        return search_result



if __name__ == '__main__':

    g = XlsOp.get_data_generator()

