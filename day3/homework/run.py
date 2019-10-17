# Author:haha
from day3.homework.choose_method import ChooseMethod

class Run:
    def __init__(self):
        self.choose_method=ChooseMethod()

    def run(self):
        choose_way=input('请输入操作方法：a(add)/d(delete)/s(select)')
        self.choose_method.choose_method(choose_way)


if __name__ == '__main__':
    add_data={'backend': 'www.oldb2oy.org','record':{'server': '100.1.7.9','weight': 20,'maxconn': 30}}
    select_data='www.oldboy.org'
    run=Run()
    run.run()