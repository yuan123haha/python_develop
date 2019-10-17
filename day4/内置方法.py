# Author:haha

print('all:',all([2,0,6]))#数据内，有假，就为假
print('any:',any([2,0,6]))#数据内，有真，就为真
print('bin:',bin(8))#将十进制转为二进制
print('hex:',hex(8))#将十进制转成十六进制
print('oct:',oct(8))#将十进制转成八进制
def test():pass
print('callable:',callable(test))#判断数据是否可以调用
print('chr:',chr(77))#输入ASCII码，找出对应字符
print('ord:',ord('m'))#输入字符，找出对用ASCII码
print('dir:',dir([]))#取出数据有哪些方法
print('ecal:',eval("{'name':'haha'}"))#将字符串转成表达式
print('pow:',pow(2,8))#取出指定数据的指定次幂
print('round:',round(2.445,2))#保留几位小数

a=bytearray('456778',encoding='utf-8')
print(a)
print(a[0])
a[0]=99
print(a)#修改字符串
#输出：
# bytearray(b'456778')
# 52
# bytearray(b'c56778')

res=filter(lambda n:n>5,range(10))#
for i in res:
    print(i)
#输出：
# 6
# 7
# 8
# 9
res2 = map(lambda n: n > 5, range(10))#
for i in res2:
    print(i)
#输出：
# False
# False
# False
# False
# False
# False
# True
# True
# True
# True
from functools import reduce
res3=reduce(lambda x,y:x+y,range(100))
print(res3)
#输出：
# 4950
print('frozenset:',frozenset([1,23,4,3,5,7,1]))#冻结集合，使集合不能更改

a={3:4,-6:3,2:7}
print(sorted(a.items()))#使字典变为列表按key值排序
print(sorted(a.items(),key=lambda x:x[1]))#使字典变为列表按value值排序
#输出：
# [(-6, 3), (2, 7), (3, 4)]
# # [(-6, 3), (3, 4), (2, 7)]

a=[1,2,3,4,5,6]
b=['a','b','c','d']
for i in zip(a,b):
    print(i)
#输出：
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, 'd')