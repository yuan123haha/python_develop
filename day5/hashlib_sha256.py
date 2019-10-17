# Author:haha

import hashlib

sh=hashlib.sha256()
sh.update(b'hello')
print(sh.hexdigest())
sh.update("It's me,哈哈".encode(encoding='utf-8'))
print(sh.hexdigest())

#验证
sh2=hashlib.sha256()
sh2.update("helloIt's me,哈哈".encode(encoding='utf-8'))
print(sh2.hexdigest())
#输出：
'''
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
69bb59a9dd5d6b843423ddcbdf050aae0c0023d858dfe66a9b3edf3253791ec6
69bb59a9dd5d6b843423ddcbdf050aae0c0023d858dfe66a9b3edf3253791ec6
'''