# Author:haha

#python中函数定义方法
def test(x):
    'The function definitions'
    x+=1
    return
'''
def:定义函数的关键字
test：函数名
（）：内可定义形参
'':函数描述（非必要，但是强烈建议为你的函数添加描述信息）
x+=1：泛指代码块或程序处理逻辑
return:定义返回值
'''
#默认参数特点：调用函数的时候，默认参数非必须传递
def test1(x=1):
    print('test1',x)
test1()
#输出：1

#接收N个位置参数，转换成元组形式
def test2(*args):
    print(args)
    print(type(args))

test2(1,2,3,4)
test2(*[1,2,3,4,5])
#输出：(1, 2, 3, 4)
#      <class 'tuple'>
    # (1, 2, 3, 4, 5)
    # <class 'tuple'>

#**kwargs:把N个关键字参数，转换成字典的方式
def test3(name,age=18,**kwargs):
    print(name)
    print(age)
    print(kwargs)

test3('haha',sex= 'm',hobby='testing')
#输出：
# haha
# 18
# {'sex': 'm', 'hobby': 'testing'}

def test4(**kwargs):
    print(kwargs)
test4(**{'name':'haha','sex':'m'})
#输出：{'name': 'haha', 'sex': 'm'}