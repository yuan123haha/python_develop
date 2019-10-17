# Author:haha

import hashlib

md=hashlib.md5()
md.update(b'hello')
print(md.hexdigest())
md.update("It's me,哈哈".encode(encoding='utf-8'))
print(md.hexdigest())

#验证
md2=hashlib.md5()
md2.update("helloIt's me,哈哈".encode(encoding='utf-8'))
print(md2.hexdigest())
#输出：
'''
5d41402abc4b2a76b9719d911017c592
12c18ee8a7b5bfa3ccb0e98109f4b1ea
12c18ee8a7b5bfa3ccb0e98109f4b1ea
'''
