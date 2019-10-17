# Author:haha

from day1.homework.homework2_code.get_data import GetData
from day1.homework.homework2_code.operation_excel import OperationExcel

class LoginCheck:
    def __init__(self):
        self.getdata=GetData()
        self.opera_exl=OperationExcel()

    def check_username(self,username):
        if username in self.opera_exl.get_col_values(0):
            return self.opera_exl.get_user_row_num(username)
        else:
            print('用户不存在，请注册用户——')
            return False

    def check_passwd(self,username,passwd):
        row=self.check_username(username)
        PWD=int(self.getdata.get_passwd(row))
        if passwd ==PWD:
            return True
        else:
            print('密码错误，请重新输入信息！')
            return False

    def check_islock(self,username):
        row=self.check_username(username)
        islock=self.getdata.get_islock(row)
        if islock=='n':
            return True
        else:
            return False

    def lock_user(self,username):
        row=self.check_username(username)
        self.opera_exl.write_data(row,col=2,value='y')

    def login(self):
        username = input('username:')
        for i in range(3):
            if self.check_username(username):
                if self.check_islock(username):
                    passwd=int(input('passwd:'))
                    if self.check_passwd(username,passwd):
                        print('登录成功！')
                        break
                else:
                    print('用户已被锁，请联系客服解锁！')
                    break
            else:
                break
        else:
            print('连续三次密码输入错误，用户已被锁，请联系客服进行解锁！')
            self.lock_user(username)



if __name__ == '__main__':
    login_check=LoginCheck()
    login_check.login()
