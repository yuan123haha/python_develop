# Author:haha

from .db_handler import Db_Handler
class Db_Account:
    def __init__(self):
        self.db_handler=Db_Handler()
    def select_account(self,account):
        '''
        查询用户信息
        :param account:
        :return:
        '''
        db_api=self.db_handler.db_handler()
        account_data,flag=db_api('select * from accounts where account=%s'%account)
        return account_data,flag

    def update_account(self,account_data):
        '''
        更新用户信息
        :param account_data:
        :return:
        '''
        db_api=self.db_handler.db_handler()
        db_api('update accounts where account=%s'%account_data['id'],account_data=account_data)