# Author:haha
import shutil

# f1=open('buweixia',encoding='utf-8')
# f2=open('buweixia2','w',encoding='utf-8')
# shutil.copyfileobj(f1,f2)#将文件内容拷贝到另一个文件中，可以部分内容

# shutil.copyfile('buweixia2','buweixia3')#拷贝文件，不用自己打开文件

import os
# print(os.stat('buweixia2'))
# shutil.copystat('buweixia2','buweixia3')#拷贝状态的信息，包括：mode bits, atime, mtime, flags
# print(os.stat('buweixia3'))
#输出：
# os.stat_result(st_mode=33206, st_ino=1688849860284406, st_dev=508939, st_nlink=1, st_uid=0, st_gid=0, st_size=1785, st_atime=1566120930, st_mtime=1566121662, st_ctime=1566120930)
# os.stat_result(st_mode=33206, st_ino=2251799813705719, st_dev=508939, st_nlink=1, st_uid=0, st_gid=0, st_size=1785, st_atime=1566120930, st_mtime=1566121662, st_ctime=1566121586)

# shutil.copy('buweixia3','buweixia4')#拷贝文件和权限
# shutil.copy2('buweixia3','buweixia5')#拷贝文件和状态信息
# print(os.stat('buweixia3'))
# print(os.stat('buweixia5'))

# shutil.copytree('./copy_file','./haha')#递归的去拷贝文件
# shutil.rmtree('./copy_file.zip')#递归的去删除文件
# shutil.move('./enen', './copy_file')#递归的去移动文件,且可以重命名目录
shutil.make_archive('./tar_file','tar')
