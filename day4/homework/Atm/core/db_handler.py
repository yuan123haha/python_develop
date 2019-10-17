# Author:haha

from ..conf import setting
import os,json

class Db_Handler:

    def db_handler(self):
        '''
        根据引擎，并返回操作函数内存信息，以便之后运行
        :return:
        '''
        db_param=setting.database
        if db_param['engine']=='file_storage':
            return self.file_storage_handle
        elif db_param['engine']=='mysql':
            pass

    def file_storage_handle(self,sql,**kwargs):
        '''
        根据sql语句类型执行
        查询语句，返回用户信息
        更新语句，返回状态
        :param sql:
        :param kwargs:
        :return:
        '''
        account_flag=False
        db_param=setting.database
        db_path='%s\%s'%(db_param['path'],db_param['name'])
        sql_list=sql.split('where')
        if sql_list[0].startswith('select'):
            column,value=sql_list[1].split('=')
            account_file='%s\%s.json'%(db_path,value)
            if os.path.isfile(account_file):
                account_flag=True
                with open(account_file,'r') as f:
                    return json.load(f),account_flag
            else:
                return None,account_flag

        elif sql_list[0].startswith('update'):
             column,value=sql_list[1].split('=')
             account_file='%s\%s.json'%(db_path,value)
             print(account_file)
             if os.path.isfile(account_file):
                 account_data=kwargs.get('account_data')
                 with open(account_file,'w') as f:
                     json.dump(account_data,f)
                 return True