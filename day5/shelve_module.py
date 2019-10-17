# Author:haha

import shelve

f=shelve.open('./copy_file/buwexia')
# print(f.get('test'))
# print(f.get('name'))
# print(f.get('info'))
info={'age':24,'sex':'m'}
name=['haha','enen','yoyo']
test=(1,2,3,4)
f['test']=test
f['name']=name
f['info']=info
f.close()