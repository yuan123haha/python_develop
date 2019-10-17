# Author:haha
from .operation_excel import OperationExcel
from .get_data import GetData
from ...Atm.core.mian import Run,user_data,access_logger
class Buyer:
    def __init__(self):
        self.data=GetData()
        self.opera_exl=OperationExcel()
        self.run=Run()

    def commodity_lists(self,commodity_list):
        for i in range(1,self.opera_exl.get_rows()):
            commodity_list.append(self.opera_exl.get_row_values(i))
        return commodity_list

    def addin_bought_car(self,my_bought_car,commodity_list,sum_amount):
        flag=None
        commodity_ID=input('请输入商品ID：')
        if commodity_ID.isdigit():
            commodity_ID=int(commodity_ID)
            if commodity_ID<len(commodity_list) and commodity_ID>=0:
                my_bought_car.append(commodity_list[commodity_ID])
                sum_amount=commodity_list[commodity_ID][1]+sum_amount
                print('将%s添加到购物车'%commodity_list[commodity_ID])
                write_commodity=OperationExcel(sheetid=1)
                write_commodity.write_data(write_commodity.get_rows(),0,commodity_list[commodity_ID][0])
                write_commodity.write_data(write_commodity.get_rows(),1,commodity_list[commodity_ID][1])
                flag=True
        elif commodity_ID=='ok':
            bought_car_flag=self.settlement_bought_car(my_bought_car,sum_amount)
            if bought_car_flag:
                my_bought_car=[]
                sum_amount=0
                choose_flag=True
                while choose_flag:
                    choose_continue=input('结算成功，是否继续购买？y(yes)/n(no):')
                    if choose_continue=='y':
                        flag=True
                        choose_flag=False
                    elif choose_continue=='n':
                        flag=False
                        choose_flag=False
                    else:
                        print('输入错误，请重新输入！')
            else:
                flag=False
        else:
            print('请输入正确商品ID号')
            flag=True
        return my_bought_car,sum_amount,flag

    def settlement_bought_car(self,my_bought_car,sum_amount):
        bought_car_flag=False
        if my_bought_car:
            print('购物车订单：%s,总金额为：%s,信用卡付款--->'%(my_bought_car,sum_amount))
            self.run.consume(sum_amount,user_data=user_data,access_logger=access_logger)
            bought_car_flag=True
        else:
            print('你未购买任何商品，再见!')
            bought_car_flag=False
        return bought_car_flag

    def shopping(self):
        flag=True
        my_bought_car = []
        sum_amount = 0
        while flag:
            commodity_list=self.commodity_lists(commodity_list=[])
            for index,item in enumerate(commodity_list):
                print(index,item)
            my_bought_car,sum_amount,flag=self.addin_bought_car(my_bought_car,self.commodity_lists(commodity_list),sum_amount)
        return flag

if __name__ == '__main__':
    shopping=Buyer()
    shopping.shopping()
