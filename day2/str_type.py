# Author:haha
name='ha\tha'
print('name:',name)
print('len(name):',len(name))
print('name.capitalize():',name.capitalize())#首部大写
print("name.count('h'):",name.count('h'))#指定字母出现的次数
print("name.center(10,'-'):",name.center(10,'-'))#指定字符串的长度，将原本的字符串数据放在中间，不够的数据用‘-’补全
print("name.ljust(10,'-'):",name.ljust(10,'-'))#指定字符串的长度，将原本的字符串数据放在左边，不够的数据用‘-’补全
print("name.rjust(10,'-'):",name.rjust(10,'-'))#指定字符串的长度，将原本的字符串数据放在右边，不够的数据用‘-’补全
print("name.endswith('a'):",name.endswith('a'))#判断字符串是否是指定字母结尾
print('name.expandtabs(tabsize=6):',name.expandtabs(tabsize=6))#将tab键转换为指定个数的空格
print("name.find('a'):",name.find('a'))#找出指定字母的指针
print("name[name.find('a'):]:",name[name.find('a'):])#切片
name2='hello {haha} world'
print('name2:',name2)
print("name2.format(haha='enen'):",name2.format(haha='enen'))
print("name2.format_map({'haha':'enen'}):",name2.format_map({'haha':'enen'}))#通过字典传参
print("'---'.join(['1','2','3']):",'---'.join(['1','2','3']))#将列表转换为字符串并用制动数据隔开
print("'HINIjijhijHI'.lower():",'HINIjijhijHI'.lower())#将大写变小写
print("'HINIjijhijHI'.lower():",'HINIjijhijHI'.lower())
print(r'\nHINIjijhijHI','\nHINIjijhijHI')
print(r"'   \nHINIjijhijHI   '.lstrip():",'   \nHINIjijhijHI   '.lstrip())#去掉最左边的回车键
print(r"'  HINIjijhijHI\n   '.rstrip():",'  HINIjijhijHI\n   '.rstrip())#去掉最右边的回车键
print(r"'   \nHINIjijhijHI   \n'.strip():",'   \nHINIjijhijHI   \n'.strip())#去掉左右的的回车键和空格键

p=str.maketrans('nbyaneuf','09754216')#通过对应数据对字符串进行替换
print('yuan'.translate(p))

print("'HINIjijhijHI'.replace('H','8',1):",'HINIjijhijHI'.replace('H','8',1))#替换指定个数的字符串内数据
print("'1+2+3+4'.split('+'):",'1+2+3+4'.split('+'))#通过字符串内指定数据对字符串进行分割，分割成列表
print("'Haha'.swapcase():",'Haha'.swapcase())#交换字符串大小写
print("'aha yoy'.title():",'aha yoy'.title())#将字符串换成标题格式，每个单词首字母大写


