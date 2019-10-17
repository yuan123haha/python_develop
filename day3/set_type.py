# Author:haha

list_1=[1,4,2,6,7,9,0,7,4,3,0]
list_1=set(list_1)
print('list1',list_1)
list_2=set([2,3,4,55,7,332])
print('list2',list_2)
list_3=set([0,1])
print('list_3',list_3)
#关系测试
print(list_1.intersection(list_2))#取交集
print('&交集',list_1&list_2)

print(list_1.union(list_2))#并集
print('|并集',list_1|list_2)

print(list_1.difference(list_2))#差集，list_1有，list_2没有的数据
print('1-2:-差集',list_1-list_2)

print(list_2.difference(list_1))#差集，list_2有，list_1没有的数据
print('2-1:-差集',list_2-list_1)

print(list_3.issubset(list_1))#判断list_3是否是list_1的子集
print(list_1.issuperset(list_3))#判断list_1是否是list_3的父集

print(list_1.symmetric_difference(list_2))#对称差集，将list_1、list_2中都互相没有的取都出来
print('^对称差集',list_1^list_2)

#其他遗漏关系
print('----------')
list_4=set([0,3])
print(list_3.isdisjoint(list_4))#判断list3是否和list4有交集，如果有，返回FALSE

list_3.add(999)
print('add 1项',list_3)
list_3.update([5,6,7])
print('update 多项',list_3)
#如果该元素不存在于集合中，则会抛出KeyError；如果存在集合中，则会移除该元素并返回None。
print('remove指定删除元素',list_3.remove(7))
#如果该元素不存在于集合中，则不会抛出KeyError；如果存在集合中，则会移除该元素并返回None。
print('discard指定删除元素',list_3.discard(5))

print('pop随机删除元素，并返回被删除的元素',list_3.pop())
print('len',len(list_3))
print(list_3)
