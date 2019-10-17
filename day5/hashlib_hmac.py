# Author:haha

import hmac

h=hmac.new("hello',b'It's me,哈哈".encode(encoding='utf-8'))
print(h.hexdigest())
#输出：4c241f49f6acc0c8669d33a4ed805cd6