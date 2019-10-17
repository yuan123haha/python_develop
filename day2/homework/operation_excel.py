# Author:haha
import xlrd
from xlutils.copy import copy

class OperationExcel:
    def __init__(self, file_name=None, sheetid=None):
        if file_name:
            self.file_name = file_name
        else:
            self.file_name = './commodity_info.xls'
        if sheetid:
            self.sheetid = sheetid
        else:
            self.sheetid = 0
        self.table = self.get_table()

    def get_table(self):
        read_data = xlrd.open_workbook(self.file_name)
        table = read_data.sheet_by_index(self.sheetid)
        return table

    def get_rows(self):
        rows = self.table.nrows
        return rows

    def get_cols(self):
        cols=self.table.ncols
        return cols

    def get_cell_values(self, row, col):
        return self.table.cell_value(row, col)

    def get_row_values(self, row):
        return self.table.row_values(row)

    def get_col_values(self, colid=0):
        if colid == 0:
            col_values = self.table.col_values(0)
        else:
            col_values = self.table.col_values(colid)
        return col_values

    def get_data_row_num(self, username):
        num = 0
        data_values = self.get_col_values()
        for data_value in data_values:
            if username in data_value:
                return num
            num += 1

    def write_data(self, row, col, value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheetid)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

if __name__ == '__main__':
    oper_exl=OperationExcel()
    for i in range(oper_exl.get_rows()):
        print(oper_exl.get_row_values(i))