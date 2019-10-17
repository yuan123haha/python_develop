# Author:haha

class ChooseMethod:
    def __init__(self,file_name=None):
        if file_name:
            self.file_name=file_name
        else:
            self.file_name='./haproxy'

    def add_data(self):
        input_data=input('请输入要添加的数据：')
        data=eval(input_data)
        with open(self.file_name,'r') as f1,\
            open(self.file_name,'a') as f2:
            flag=self.base(data['backend'])
            if flag==False:
                f2.write('\nbackend %s\n'%data['backend'])
                f2.write('\t\tserver %s weight %s maxconn %s\n'%(data['record']['server'],data['record']['weight'],data['record']['maxconn']))


    def select_data(self):
        input_data=input('请输入要查询的数据：')
        data='backend %s\n'%input_data
        flag=self.base(data)
        return flag

    def base(self,data):
        flag = False
        Flag = False
        with open(self.file_name,'r') as f:
            for line in f:
                if data in line:
                    flag=True
                    Flag=True
                    print('内容已存在')
                elif 'backend ' in line and flag == True:
                    flag = False
                while flag:
                    print(line)
                    break
            if Flag==False:
                print('内容不存在')
        return Flag

    def delete_data(self):
        flag=False
        Flag=False
        input_data=input('请输入要删除的数据：')
        data=eval(input_data)
        with open(self.file_name,'r+') as f1, \
                open('./haha', 'w') as f2:
            data='backend %s\n'%data['backend']
            print(data)
            for line in f1:
                if data in line:
                    flag = True
                    print('内容存在，正在删除')
                    Flag=True
                elif 'backend ' in line and flag == True:
                    flag = False
                while flag==False:
                    f2.write(line)
                    break
            if Flag==False:
                print('内容不存在')

    def choose_method(self,method):
        if method=='a':
            self.add_data()
        elif method=='d':
            self.delete_data()
        elif method=='s':
            self.select_data()
        else:
            print('输入错误，请重新输入')


if __name__ == '__main__':
    choose_method=ChooseMethod()
    add_data={'backend': 'www.oldb2oy.org','record':{'server': '100.1.7.9','weight': 20,'maxconn': 30}}
    select_data='www.oldboy.org'
    # choose_method.select_data()
    # choose_method.add_data()
    choose_method.delete_data()