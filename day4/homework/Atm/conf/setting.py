# Author:haha
import os
import logging
LOG_LEVEL=logging.INFO

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)
LOG_TYPES={
    'transaction': 'transactions.log',
    'access': 'access.log',
}

database={
    'engine':'file_storage',
    'name':'accounts',
    'path':'%s\db'%base_dir
}
TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},#还款
    'withdraw':{'action':'minus', 'interest':0.05},#取现
    'transfer':{'action':'minus', 'interest':0.05},#转账
    'consume':{'action':'minus', 'interest':0},#消费

}