# Author:haha
info={
    'name':'haha',
    'age':12,
    'sex':'female'
      }
info['name']='enen'#修改现有数据
print(info)
info['ID']='1'#添加数据
print(info)
print(info.keys())#打印所有的key
print(info.values())#打印所有的values
info.setdefault('pp','yoyo')#字典中取key值，能取到就返回value值，没取到，就创建key值，及新value值
print(info)
print('name' in info)#判断指定key是否在字典中
print(info.get('name'))#查找指定key值value，存在打印，不存在，打印none
print(info.get('oo'))
del info['ID']#删除指定key数据
print(info)
info.pop('name')#删除指定key数据
print(info)

a={'a':'aa','b':'bb','c':'cc'}
b={'a':'haha',1:11,2:22}
a.update(b)#将b合并大a中，如果有相同key值，b的value替换a中value值
print(a)
print(a.items())
c=dict.fromkeys([6,7,8],'test')#初始化字典
print(c)

#字典的循环
for i in a:#效率更高
    print(i,a[i])
for i,j in a.items():
    print(i,j)
