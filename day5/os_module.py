# Author:haha
import os

print(os.getcwd())#获取当前工作目录，即当前python脚本工作的目录路径
# os.chdir('C://')#改变当前脚本工作目录；相当于shell下cd
print(os.curdir)#返回当前目录: ('.')
print(os.pardir)#获取当前目录的父目录字符串名：('..')
os.makedirs(r'd:\a\b\c')#可生成多层递归目录
os.removedirs(r'd:\a\b\c')#若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推
os.mkdir(r'd:a')#生成单级目录；相当于shell中mkdir dirname
os.rmdir(r'd:a')# 删除单级空目录，若目录不为空则无法删除，报错；相当于shell中rmdir dirname
print(os.listdir(r'd:'))#列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印
#输出：['$360Section', '$RECYCLE.BIN', '360Downloads', '360Rec', '360安全浏览器下载', 'BaiduNetdiskDownload', 'computer software', 'Config.Msi']
# os.remove(r'd:\a')#删除一个文件
# os.rename(r'd:\a',r'd:\b')#重命名文件/目录
print(os.stat(r'd:360安全浏览器下载'))#获取文件/目录信息
#输出：os.stat_result(st_mode=16895, st_ino=5066549580791849, st_dev=485194, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1565493157, st_mtime=1565493157, st_ctime=1563296312)
print(os.sep)#输出操作系统特定的路径分隔符，win下为"\\",Linux下为"/"
print(os.linesep)#输出当前平台使用的行终止符，win下为"\r\n",Linux下为"\n"
print(os.pathsep)#输出用于分割文件路径的字符串
print(os.environ)#当前系统的环境变量
print(os.name)#输出字符串指示当前使用平台。win->'nt'; Linux->'posix'
os.system('dir')#运行shell命令，直接显示
print(os.path.abspath('./'))#返回path规范化的绝对路径
print(os.path.split(r'd:a.txt'))#将path分割成目录和文件名二元组返回
#输出：('d:', 'a.txt')
print(os.path.dirname(os.path.abspath('./')))#返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.basename(os.path.abspath('./')))#返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists(os.path.abspath('./')))#判断路径是否存在，如果path存在，返回True；如果path不存在，返回False
print(os.path.isabs(os.path.abspath('./')))#判断路径是否是绝对路径
print(os.path.isfile(os.path.abspath('./')))#判断路径是否是文件
print(os.path.isdir(os.path.abspath('./')))#判断路径是否是目录
print(os.path.join(r'dir\haha',r'module',r'file'))#将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
#输出：dir\haha\module\file
import time
struct_time=time.localtime(os.path.getatime(os.path.abspath('./')))
print(time.strftime('%Y-%m-%d %H:%M:%S',struct_time))#返回path所指向的文件或者目录的最后存取时间,结果是时间戳，这里转化为字符串时间格式
#输出：2019-08-18 15:53:13
print(os.path.getmtime(os.path.abspath('./')))#返回path所指向的文件或者目录的最后修改时间
#输出：1566114793.5133495


