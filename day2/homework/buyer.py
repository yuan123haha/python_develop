# Author:haha
from day2.homework.operation_excel import OperationExcel
from day2.homework.get_data import GetData

class Buyer:
    def __init__(self):
        self.data=GetData()
        self.opera_exl=OperationExcel()

    def check_salary_commodity_info(self,salary,index):
        if salary>=self.data.get_price(index):
            return self.opera_exl.get_row_values(index)
        else:
            return False

    def commodity_lists(self,salary,commodity_list):
        for i in range(1,self.opera_exl.get_rows()):
            check_salary_commodity_info=self.check_salary_commodity_info(salary,i)
            if check_salary_commodity_info:
                commodity_list.append(check_salary_commodity_info)
        return commodity_list

    def addin_bought_car(self,my_bought_car,commodity_list,salary):
        flag=None
        commodity_ID=input('请输入商品ID：')
        if commodity_ID.isdigit():
            commodity_ID=int(commodity_ID)
            if commodity_ID<len(commodity_list) and commodity_ID>=0:
                my_bought_car.append(commodity_list[commodity_ID])
                salary=salary-commodity_list[commodity_ID][1]
                print('将%s添加到购物车，剩余金额\033[31;1m%s\033[0m'%(commodity_list[commodity_ID],salary))
                write_commodity=OperationExcel(sheetid=1)
                write_commodity.write_data(write_commodity.get_rows(),0,commodity_list[commodity_ID][0])
                write_commodity.write_data(write_commodity.get_rows(),1,commodity_list[commodity_ID][1])
                write_commodity.write_data(write_commodity.get_rows(),2,salary)
                flag=True
        elif commodity_ID=='q':
            self.quit_shopping(my_bought_car,salary)
            flag=False
        else:
            print('请输入正确商品ID号')
            flag=True
        return my_bought_car,salary,flag

    def quit_shopping(self,my_bought_car,salary):
        if my_bought_car:
            print('一共购买了',my_bought_car)
            print('余额还剩:\033[31;1m%s\033[0m'%salary)
        else:
            print('你未购买任何商品，再见！')

    def shopping(self):
        flag=True
        while flag:
            my_bought_car=[]
            salary=input('请输入工资:')
            if salary.isdigit():
                salary=int(salary)
                while self.commodity_lists(salary,commodity_list=[]):
                    commodity_list = []
                    commodity_list=self.commodity_lists(salary,commodity_list)
                    if flag:
                        for index,item in enumerate(commodity_list):
                            print(index,item)
                        my_bought_car,salary,flag=self.addin_bought_car(my_bought_car,self.commodity_lists(salary,commodity_list),salary)
                    else:
                        break
                else:
                    self.quit_shopping(my_bought_car,salary)
                    print('您的工资不足以继续买商品。。。')
            elif salary=='q':
                print('已退出')
                flag=False
                break
            else:
                print('请输入正确格式!')
        return flag

if __name__ == '__main__':
    shopping=Buyer()
    shopping.shopping()
