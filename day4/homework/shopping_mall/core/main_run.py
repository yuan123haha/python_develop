# Author:haha
from day4.homework.shopping_mall.core.buyer import Buyer
from day4.homework.shopping_mall.core.seller import Seller

class Run_test:
    def __init__(self):
        self.buyer=Buyer()
        self.seller=Seller()

    def user_case(self):
        flag = True
        while flag:
            user_car = input('请输入用户身份：s(seller)/b(buger)')
            if user_car == 'b':
                flag=self.buyer.shopping()
            elif user_car == 's':
                flag=self.seller.choose_do()
            elif user_car=='q':
                print('已退出')
                break
            else:
                print('输如错误，请重新输入：')

if __name__ == '__main__':
    run=Run_test()
    run.user_case()