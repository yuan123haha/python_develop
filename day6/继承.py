# Author:haha

#class Peple(object):#新式类
class Peple:#经典类
    def __init__(self,name):
        self.name=name
        self.friend=[]
    def sleep(self):
        print('%s sleep...'%self.name)

    def eat(self):
        print('%s eat...'%self.name)

class Relation(object):
    def make_friends(self,obj):
        print('%s make friends with %s'%(self.name,obj.name))
        self.friend.append(obj)#传的是对象内存，而不是值
class Man(Peple,Relation):#多继承
    def __init__(self,name,age):#添加实例参数
        # Peple.__init__(self,name)#经典类
        super(Man,self).__init__(name)#新式类
        self.age=age
        print('%s age:%s'%(self.name,self.age))
    def work(self):
        print('%s work...'%self.name)

    def make_monkey(self):#调用父类函数
        Peple.sleep(self)
        print('%s make_money...'%self.name)

class Woman(Peple):#继承Peple
    def shopping(self):
        print('%s shopping...'%self.name)

m=Man('haha',3)
m.eat()
m.make_monkey()
w=Woman('enen')
w.shopping()
m.make_friends(w)
w.name='yoyo'
print(m.friend[0].name)
