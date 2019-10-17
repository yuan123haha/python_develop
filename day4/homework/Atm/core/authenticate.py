# Author:haha

from .db_account import Db_Account


def login_check(func):
    '''
    用户登录检查装饰器，如果没有登录，则进入登录操作
    :param func:
    :return:
    '''
    def wrapper(*args,**kwargs):
        if kwargs.get('user_data')['is_authenticated']:
            return func(*args,**kwargs)
        else:
            print('\033[31;1m你还未登录！请登录：\033[0m')
            auth=Authenticate()
            account_data =auth.authenticate_login(kwargs.get('user_data'), kwargs.get('access_logger'))
            if kwargs.get('user_data')['is_authenticated']:
                kwargs.get('user_data')['acoount_data'] = account_data
            return func(*args,**kwargs)
    return wrapper

class Authenticate:
    def __init__(self):
        self.db_account = Db_Account()
    def check_accountdata(self,account,passwd):
        '''
        检查登录信息
        :param account:
        :param passwd:
        :return:
        '''
        account_data,flag=self.db_account.select_account(account)
        if flag:
            if account_data['password']==passwd:
                return account_data
            else:
                print('\033[31;1myour account or passed is incorrect!\033[0m')
        else:
            print('\033[31;1maccount [%s] does not exist!\033[0m' % account)

    def authenticate_login(self,user_data,log_object):
        '''
        用户登录
        :param user_data:
        :param log_object:
        :return:
        '''
        count=0
        while user_data['is_authenticated'] is False and count<3:
            account=input('your account:')
            passwd=input('your passwd:')
            account_data=self.check_accountdata(account,passwd)
            if account_data:
                user_data['is_authenticated']=True
                user_data['account_id']=account
                return account_data
            count+=1
        else:
            log_object.error('account [%s] too many login attempts'%account)
            exit()

