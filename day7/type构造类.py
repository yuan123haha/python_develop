# Author:haha

def func(self):
    print('hello[%s]this is func!'%self.name)

def __init__(self,name):
    self.name=name

f=type('Foo',(object,),{'welcome':func,'__init__':__init__})
h=f('haha')
h.welcome()