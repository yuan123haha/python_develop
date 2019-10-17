# Author:haha
import time
def eat(name):
    print('%s,来了，点了包子'%name)
    while True:
        num=yield
        print('%s正在吃了第%s个包子'%(name,num))


def make():
    c=eat('A')
    c2=eat('B')
    c.__next__()
    c2.__next__()
    print('包子拿来了')
    time.sleep(1)
    for i in range(8):
        time.sleep(1)
        print('上了第%s个包子'%i)
        c.send(i)
        c2.send(i)

make()