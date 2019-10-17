# Author:haha
'''
def cals(max):
    n=0
    a=0
    b=1
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'done'

print(cals(10))
'''

def cals(max):
    n=0
    a=0
    b=1
    print('yoyo')
    while n<max:
        yield b
        a,b=b,a+b
        n+=1
    return 'done'
c=cals(6)
while True:
    try:
        print(next(c))
    except StopIteration as s:
        print('StopIteration',s.value)
        break
