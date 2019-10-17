# Author:haha
from day1.homework.homework2_code.data_config import DataConfig
from day1.homework.homework2_code.operation_excel import OperationExcel

class GetData:
    def __init__(self):
        self.opera_exl=OperationExcel()
        self.dataconfig=DataConfig()

    def get_username(self,row):
        col=int(self.dataconfig.get_username_id())
        return self.opera_exl.get_cell_values(row,col)

    def get_passwd(self,row):
        col=int(self.dataconfig.get_passwd_id())
        return self.opera_exl.get_cell_values(row,col)

    def get_islock(self,row):
        col=int(self.dataconfig.get_islock_id())
        return self.opera_exl.get_cell_values(row,col)
