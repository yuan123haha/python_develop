# Author:haha

def talk(self):
    print('%s is talking...'%self.name)

class Foo(object):
    def __init__(self,name):
        self.name=name

    def eat(self,food):
        print('%s is eating %s'%(self.name,food))

f=Foo('haha')
a='eat'
b='talking'
c='name'
'''
hasattr(obj,name_str),判断一个对象obj里是否有对应的name_str字符串的方法
'''
print(hasattr(f,a))
#输出：True
print(hasattr(f,b))
#输出：False
print(hasattr(f,c))
#输出：True
'''
getattr(obj,name_str),根据字符串去获取obj对象里的对应的方法的内存地址
'''
print(getattr(f,a))
#输出：<bound method Foo.eat of <__main__.Foo object at 0x0000000001E08F98>>
getattr(f,a)('包子')
#输出：haha is eating 包子
print(getattr(f,c))
#输出：haha

'''
setattr(obj,name_str,z),在obj对象里根据字符串创建新的方法，z代表已有的方法或实例参数
'''
setattr(f,b,talk)
f.talking(f)
#输出：haha is talking...

setattr(f,b,22)
print(f.talking)
#输出：22

'''
delattr(obj,name_str),删除obj对象里对应的字符串方法或实例参数
'''
delattr(f,a)
f.eat('馒头')
#输出：报错：AttributeError: eat

delattr(f,c)
f.name
#输出：报错：AttributeError: 'Foo' object has no attribute 'name'