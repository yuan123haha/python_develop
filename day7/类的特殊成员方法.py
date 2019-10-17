# Author:haha
class Fo(object):
    n='enen'
    def __init__(self,name):
        self.name=name
    def func(self):
        pass
    def __call__(self, *args, **kwargs):
        print('running',args,kwargs)
    def __str__(self):
        return 'obj：%s'%self.name
Fo('haha')(1,2,3,age=22)
#输出：running (1, 2, 3) {'age': 22}
print(Fo.__dict__)#打印类里的所有属性，不包括实例对象
#输出：{'__module__': '__main__', 'n': 'enen', '__init__': <function Fo.__init__ at 0x00000000021EA950>, 'func': <function Fo.func at 0x00000000021EA8C8>, '__call__': <function Fo.__call__ at 0x00000000021EAC80>, '__dict__': <attribute '__dict__' of 'Fo' objects>, '__weakref__': <attribute '__weakref__' of 'Fo' objects>, '__doc__': None}
print(Fo('haha').__dict__)#打印所有实例对象，不包括类属性
#输出：{'name': 'haha'}
print(Fo('haha'))
#输出：obj：haha