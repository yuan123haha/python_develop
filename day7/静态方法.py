# Author:haha

class Person(object):
    n='enen'
    def __init__(self,name):
        self.name=name

    @staticmethod
    def eat(food):
        #静态方法已经和类没有关系了
        #知识名义上归类管理，实际上在静态方法里访问不了类或实例中的任何属性
        print('eat %s'%food)

    @property#属性方法就是把一个方法变成一个静态属性
    def sleep(self):
        print('%s is sleeping...'%self.name)

    @sleep.setter
    def sleep(self,new_name):
        print('%s change to %s'%(self.name,new_name))
        self.name=new_name

    @sleep.deleter
    def sleep(self):
        print('delete sleep...')

    @classmethod
    def talk(self,talking):
        #类方法只能访问类变量，不能访问实例变量
        print('%s talk "%s"'%(self.n,talking))

person=Person('haha')
person.eat('包子')
person.talk('hhhhhhh')
person.sleep='yoyo'
person.sleep
del person.sleep#触发 @sleep.deleter
#输出：
'''eat 包子
enen talk "hhhhhhh"
haha change to yoyo
yoyo is sleeping...
delete sleep...
yoyo is sleeping...
'''