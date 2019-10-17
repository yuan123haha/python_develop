# Author:haha

'''
#读文件
file=open('buweixia','r',encoding='utf-8')#文件句柄,默认读模式
data=file.read()#执行后文件指针已经知道文件末尾
data2=file.read()#所以data2为空
print(data)
print('---data2---',data2)
file.close()

#写文件
file2=open('buweixia2','w',encoding='utf-8')#使用写模式，是创建，如果文件存在，就会覆盖之前内容，如果文件不存在，就会创建文件
file2.write('不谓侠\n')
file2.write('歌词\n')
file2.close()

file7=open('buweixia2','wb')#以二进制模式写文件
file7.write('编曲：潮汐-tide\n')
file7.close()
'''
'''
#可读可写
file5=open('buweixia2','r+',encoding='utf-8')#使用写模式，是创建，如果文件存在，就会覆盖之前内容，如果文件不存在，就会创建文件
print(file5.readline().strip())
print(file5.readline().strip())
file5.write('不谓侠\n')
file5.write('歌词\n')
file5.close()

file6=open('buweixia2','rb')#以二进制模式读取文件
print(file6.readline().strip())
print(file6.readline().strip())
'''

'''
#追加文件
file3=open('buweixia2','a',encoding='utf-8')#使用追加模式，是创建，如果文件存在，就会覆盖之前内容，如果文件不存在，就会创建文件
file3.write('词：迟意 ')
file3.write('曲：潮汐-tide\n')
file3.close()
'''

'''
#循环文件,大文件的话，占内存
file4=open('buweixia','r',encoding='utf-8')#文件句柄,默认读模式
#打印前5行内容
print('------打印前5行内容------')
for i in range(5):
    print(file4.readline().strip())

print('--------循环文件，操作第10行---------')
for index,line in enumerate(file4.readlines()):
    if index==9:
        print('-----分割线-------')
        continue
    print(line.strip())
'''
'''
#高效循环文件，不占内存
file4=open('buweixia','r',encoding='utf-8')#文件句柄,默认读模式
count=0
for line in file4:
    if count==9:
        print('-----分割线-------')
        count += 1
        continue
    count+=1
    print(line.strip())
'''

'''
file=open('buweixia','r',encoding='utf-8')#文件句柄,默认读模式
print(file.tell())#打印当前指针的位置
print(file.read(5))#指定读取文件字符个数
print(file.tell())
file.seek(22)#移动指针到文件开头位置
print(file.readline())
print(file.encoding)#打印文件的编码格式
print(file.name)#打印文件名

print(file.flush())#实时更新硬盘数据
#例：
import sys,time
for i in range(10):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)

file.truncate(10)#没有参数，就清空文件；有参数，就从指定指针位置截断文件
'''

#修改文件
f1=open('buweixia','r',encoding='utf-8')
f_new=open('buweixia_update','w',encoding='utf-8')
for line in f1:
    if '潮汐-tide' in line:
        line=line.replace('潮汐-tide','haha')
    f_new.write(line)
f1.close()
f_new.close()

#with语句
with open('buweixia','r',encoding='utf-8') as f,\
        open('buweixia','r',encoding='utf-8') as f2:
    for line in f:
        print(line)
    print(f2.readline())