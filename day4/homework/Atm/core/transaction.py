# Author:haha

from ..conf import setting
from .db_account import Db_Account

class Transaction:
    def __init__(self):
        self.db_account=Db_Account()

    def do_transaction(self,amount,tran_type,user_data,log_obj):
        '''
        执行用户选择的信用卡业务，对用户信息的可用额度进行更新
        :param amount:
        :param tran_type:
        :param user_data:
        :param log_obj:
        :return:
        '''
        amount=float(amount)
        if tran_type in setting.TRANSACTION_TYPE:
            interest=amount*setting.TRANSACTION_TYPE[tran_type]['interest']
            old_available_credit=user_data['acoount_data']['Available_credit']
            if setting.TRANSACTION_TYPE[tran_type]['action']=='plus':
                new_available_credit=amount+old_available_credit
            elif setting.TRANSACTION_TYPE[tran_type]['action']=='minus':
                new_available_credit = old_available_credit-amount-interest
                if new_available_credit<0:
                    print('\033[31;1mYour available_credit[%S] is not enough for this transaction[%s]!\033[0m'%(old_available_credit,amount+interest))
                    return

            user_data['acoount_data']['Available_credit']=float('%0.2f'%new_available_credit)
            self.db_account.update_account(user_data['acoount_data'])
            log_obj.info('\033[32;1maccount:%s   action:%s    amount:%s   interest:%s\033[0m'%(user_data['account_id'],tran_type,amount,interest))
            return user_data['acoount_data']
        else:
            print('\033[31;1mTransaction type [%s] is not exist!\033[0m'%tran_type)
            return None



