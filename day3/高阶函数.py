# Author:haha
def add(a,b,f):
    return f(a)+f(b)

res=add(2,-6,abs)
print(res)
#输出：8