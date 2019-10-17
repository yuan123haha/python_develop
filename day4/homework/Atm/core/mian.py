# Author:haha
import sys,os
base_dir=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(base_dir)

from day4.homework.Atm.core.authenticate import login_check
from day4.homework.Atm.core.transaction import Transaction
from day4.homework.Atm.core.logger import logger
from day4.homework.Atm.core.db_account import Db_Account
#访问日志
access_logger = logger('access')
user_data = {
    'account_id': None,
    'is_authenticated': False,
    'acoount_data': None
}
class Run:

    def __init__(self):
        self.transaction=Transaction()
        self.db_account=Db_Account()

    def run(self):
        '''
        执行主程序，
        :return:
        '''
        self.choose_business(user_data)


    def choose_business(self,user_data):
        menu='''
        -----business list-----
        1、账户信息
        2、还款
        3、提现
        4、转账
        5、账单
        6、退出
        '''
        menu_dic={
            '1':self.account_info,
            '2':self.repay,
            '3':self.withdraw,
            '4':self.transfer,
            '5':self.pay_check,
            '6':self.logout
        }
        exit_flag=False
        while not exit_flag:
            print(menu)
            user_choose=input('>>:').strip()
            if user_choose in menu_dic:
                menu_dic[user_choose](user_data=user_data,access_logger=access_logger)
                print('user_data',user_data)
            else:
                print('\033[31;1mchoose data does not exist!\033[0m')

    @login_check
    def account_info(self,user_data=user_data,access_logger=access_logger):
        '''
        查看账户信息
        :param user_data:
        :param access_logger:
        :return:
        '''
        print('user_data',user_data)
        data_menu='''
            -----account_info-----
            account:{0}
            Available_credit:{1}
            credit:{2}
    以上为您的账户信息，请选择您接下来的操作---->
        '''.format(user_data['account_id'],user_data['acoount_data']['Available_credit'],user_data['acoount_data']['credit'])
        print(data_menu)

    @login_check
    def transfer(self,user_data=user_data,access_logger=access_logger):
        balance_info = '''
                -----account_info-----
            Available_credit:{0}
            credit:{1}
        '''.format(user_data['acoount_data']['Available_credit'], user_data['acoount_data']['credit'])
        print(balance_info)
        back_flag = False
        while not back_flag:
            tran_to_account=input('\033[33;1mInput transfer to account:\033[0m')
            if  tran_to_account== 'b':
                    back_flag = True
            else:
                transfer_to_account_data,flag=self.db_account.select_account(tran_to_account)
                if flag:
                    amount = input('\033[33;1mInput transfer amount:\033[0m')
                    if amount.isdigit() and float(amount)>0:
                        account_data = self.transaction.do_transaction(amount, 'transfer', user_data, log_obj=access_logger)
                        transfer_to_account_data['Available_credit']=transfer_to_account_data['Available_credit']+float(amount)
                        self.db_account.update_account(transfer_to_account_data)
                        if account_data:
                            print('\033[42;1mNew Balance:%s\033[0m' % account_data['Available_credit'])
                    elif amount == 'b':
                        back_flag = True
                    else:
                        print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % amount)
                else:
                    print('\033[31;1mtransfer to account [%s] does not exist!\033[0m'%tran_to_account)

    @login_check
    def consume(self,amount,user_data=user_data,**kwargs):
        account_data = self.transaction.do_transaction(amount, 'consume', user_data, log_obj=access_logger)
        if account_data:
            print('\033[42;1mNew Balance:%s\033[0m' % account_data['Available_credit'])
        return

    def pay_check(self):
        pass


    def logout(self,**kwargs):
        exit('see you~~~~ ')

    @login_check
    def withdraw(self,user_data=user_data,**kwargs):
        balance_info = '''
                -----account_info-----
            Available_credit:{0}
            credit:{1}
        '''.format(user_data['acoount_data']['Available_credit'], user_data['acoount_data']['credit'])
        print(balance_info)
        back_flag = False
        while not back_flag:
            amount = input('\033[33;1mInput withdraw amount:\033[0m')
            if amount.isdigit() and float(amount)>0:
                account_data = self.transaction.do_transaction(amount, 'withdraw', user_data, log_obj=access_logger)
                if account_data:
                    print('\033[42;1mNew Balance:%s\033[0m' % account_data['Available_credit'])
            elif amount == 'b':
                back_flag = True
            else:
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m' % amount)

    @login_check
    def repay(self,user_data=user_data,**kwargs):
        balance_info='''
                -----account_info-----
            Available_credit:{0}
            credit:{1}
        '''.format(user_data['acoount_data']['Available_credit'],user_data['acoount_data']['credit'])
        print(balance_info)
        back_flag=False
        while not back_flag:
            amount=input('\033[33;1mInput repay amount:\033[0m')
            if amount.isdigit() and float(amount)>0:
                account_data=self.transaction.do_transaction(amount,'repay',user_data,log_obj=access_logger)
                if account_data:
                    print('\033[42;1mNew Balance:%s\033[0m'%account_data['Available_credit'])
            elif amount=='b':
                back_flag=True
            else:
                print('\033[31;1m[%s] is not a valid amount, only accept integer!\033[0m'%amount)


if __name__ == '__main__':
    run=Run()
    run.run()