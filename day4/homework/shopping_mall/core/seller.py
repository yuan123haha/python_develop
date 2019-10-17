# Author:haha
from operation_excel import OperationExcel

class Seller:
    def __init__(self):
        self.opera_exl=OperationExcel()

    def update_commodity_info(self,flag):
        for index,i in enumerate(range(1,self.opera_exl.get_rows())):
            print(index,self.opera_exl.get_row_values(i))
        choose_id=input('请输入商品ID号：')
        if choose_id.isdigit():
            choose_id=int(choose_id)+1
            print(self.opera_exl.get_row_values(choose_id))
            updata_price=input('请输入修改后的金额：')
            if updata_price.isdigit():
                updata_price = int(updata_price)
                self.opera_exl.write_data(choose_id,1,updata_price)
                self.opera_exl=OperationExcel()
                print('修改成功',self.opera_exl.get_row_values(choose_id))
            elif updata_price == 'q':
                print('已退出')
                flag = False
            else:
                print('输入错误，请重新输入：')
        elif choose_id=='q':
            print('已退出')
            flag=False
        else:
            print('输入错误，请重新输入：')
        return flag

    def add_commodity_info(self,flag):
        for index,i in enumerate(range(1,self.opera_exl.get_rows())):
            print(index,self.opera_exl.get_row_values(i))
        add_commodity_name=input('请输入商品名称：')
        if add_commodity_name == 'q':
            print('已退出')
            flag = False
        add_commodity_price=input('请输入商品金额：')
        if add_commodity_price.isdigit():
            add_commodity_price = int(add_commodity_price)
            self.opera_exl.write_data(self.opera_exl.get_rows(), 0, add_commodity_name)
            self.opera_exl.write_data(self.opera_exl.get_rows(), 1, add_commodity_price)
            self.opera_exl = OperationExcel()
        elif add_commodity_price == 'q':
            print('已退出')
            flag = False
        else:
            print('输入错误，请重新输入：')
        return flag

    def choose_do(self):
        flag=True
        while flag:
            choose_do=input('请输入要做的操作：（u/a）')
            if choose_do=='u':
                flag=self.update_commodity_info(flag)
            elif choose_do=='a':
                flag=self.add_commodity_info(flag)
            elif choose_do=='q':
                print('已退出')
                flag=False
                break
            else:
                print('输入错误，请重新输入：')
        return flag

if __name__ == '__main__':
    seller=Seller()
    seller.choose_do()