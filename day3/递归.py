# Author:haha
def test(n):
    print(n)
    if int(n/2)>0:
        return test(int(n/2))
    print("->",n)
test(10)
#输出：
# 10
# 5
# 2
# 1
# -> 1