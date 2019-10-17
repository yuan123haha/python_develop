# Author:haha

class Role(object):
    n='123'#类参数：大家都有的属性，节省内存
    def __init__(self, name, role, weapon, life_value=100, money=15000):#构造函数
        self.name = name#实例参数，（静态属性）
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value#私有属性：类外面不可调用
        self.money = money

    def __del__(self):#析构函数：在实例释放、销毁的时候自动执行的，通常用于一些收尾工作，如关闭一些数据库连接、关闭打开的临时文件等
        print('%s 彻底死了！'%self.name)

    def shot(self):#类方法 功能（动态属性）
        print("shooting...")

    def got_shot(self):
        print("ah...,I got shot...")

    def __buy_gun(self, gun_name):#私有方法：外面不可调用
        print("just bought %s" % gun_name)


r1 = Role('Alex', 'police', 'AK47') #生成一个角色
r1.n='haha'
print('r1:',r1.n)
r2 = Role('Jack', 'terrorist', 'B22')  #生成一个角色
print('r2:',r2.n)
Role.n='abc'
print('类参数改后：r1:%s;r2:%s'%(r1.n,r2.n))
