# Author:haha
from day2.homework.data_config import DataConfig
from day2.homework.operation_excel import OperationExcel

class GetData:
    def __init__(self):
        self.opera_exl=OperationExcel()
        self.dataconfig=DataConfig()

    def get_commodity(self,row):
        col=int(self.dataconfig.get_commodity_id())
        return self.opera_exl.get_cell_values(row,col)

    def get_price(self,row):
        col=int(self.dataconfig.get_price_id())
        return int(self.opera_exl.get_cell_values(row,col))

