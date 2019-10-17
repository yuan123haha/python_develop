# Author:haha

a={'1':'a'}
# a[2]
#报错：KeyError: 2
b=[1,2,3]
# b[3]
#报错：IndexError: list index out of range
'''
try:
    a[2]
except KeyError as e:
    print (e)
#输出：2
try:
    b[3]
except IndexError as e:
    print (e)
#输出：list index out of range
'''
try:
    a[2]
    b[3]
except (KeyError,IndexError) as e:
    print (e)
except Exception as mg:
    print ('其他错误')
else:print ('一切正常')
finally:print ('不管有无错误都会执行')
#输出：
'''
2
不管有无错误都会执行
'''