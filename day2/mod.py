# Author:haha
import sys
#print(sys.path)#打印环境变量
import os
cmd_system=os.system('dir')#执行命令，不保存结果
print('cmd_system-->',cmd_system)
cmd_popen=os.popen('dir').read()#通过read方法读取存在内存的信息
print('cmd_popen--->',cmd_popen)
os.mkdir('new_dir')#在当前位置创建一个目录