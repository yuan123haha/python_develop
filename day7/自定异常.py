# Author:haha
class HahaError(Exception):
    def __init__(self,msg):
        self.massage=msg

    def __str__(self):
        return '错误类型：Haha'

try:
    raise HahaError('连接数据库。。。')
except HahaError as msg:
    print (msg)
#输出：错误类型：Haha