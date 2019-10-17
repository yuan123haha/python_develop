# Author:haha
import sys

print(sys.argv)#命令行参数List，第一个元素是程序本身路径
print(sys.version)#获取Python解释程序的版本信息
#输出：3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)]
print(sys.path)#返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
print(sys.platform)#返回操作系统平台名称
sys.exit(0)#退出程序，正常退出时exit(0)

