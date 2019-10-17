# Author:haha

#局部变量，所在函数就是这个变量的作用域
def test1(name):
    print('before change %s'%name)
    name='HAHA'
    print('after change %s'%name)

name='haha'
test1(name)
print(name)
#输出：
# before change haha
# after change HAHA
# haha

#全局变量
def test2():
    global name #申明变量的类型
    print('before change %s'%name)
    name='HAHA'
    print('after change %s'%name)

name='haha'#全局变量
test2()
print(name)
#输出：
# before change haha
# after change HAHA
# HAHA

#当参数为字典，列表，集合时，函数里面可以改全局变量
def test3():
    print('before change %s'%names)
    names[0]='HAHA'
    print('after change %s'%names)

names=['haha','yoyo','enen']#全局变量
test3()
print(names)