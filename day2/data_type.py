# Author:haha
'''
a,b,c=1,2,3
d=b if a>b else c
print(d)'''
'''
msg='欢迎'
print(msg)
msg2=msg.encode()
print(msg2)
print(msg2.decode())'''

import copy
name=['haha','enen','lala','yoyo',['yuan','jojo'],'hengheng','lala']
print(len(name))
'''
print(name[0:-1:2])#切片隔一个打印一个
#print(name[::2])#同上
name2=name.copy()#浅copy，复制第一层，其他的多层数据都是copy的内存地址
name3=copy.deepcopy(name)#深copy，全部复制，复制的就是数据
print(name3)
print(name2)
name[2]='啦啦'
print(name)
print(name2)
print(name3)
name[4][0]='YUAN'
print(name)
print(name2)
print(name3)
'''
'''
print(name[0])
print(name[2:4])#切片：顾头不顾尾，包含开头，不包含结束位置
print(name[-1])#取最后一个
print(name[-3:-1])
print(name[-2:])#取最后两个
print(name[:2])#取前面两个

name.append('qq')#插入数据到最后面
print(name)
name.insert(1,'pp')#插入数据到指定位置
print(name)

name[1]='KK'#修改指定位置的数据
print(name)

name.remove('KK')#删除指定数据
print(name)
del name[-1]#删除指定位置数据
print(name)
name.pop(1)#删除指定位置的数据，没有输入下标，默认删除最后一个数据

print(name.index('yoyo'))#查找指定数据的坐标

print(name.count('hengheng'))#查看指定数据的个数
name.reverse()#翻转列表
print(name)
name.sort()#排序（特殊符号，数字，大写字母，小写字母）
print(name)
name_num=[1,2,3,4]
name.extend(name_num)#合并2个列表
print(name,name_num)

name.clear()#清空列表
print(name)
'''
