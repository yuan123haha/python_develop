# Author:haha
'''
username='haha'
passwd='123'
def login(type):
    def outwrapper(func):
        def wrapper(*args,**kwargs):
            if type=='qq':
                name=input('your username:')
                psd=input('your password:')
                if name==username and passwd==psd:
                    print('welcome...')
                    return func(*args, **kwargs)
                else:print('username or passwd error')
            else:
                print('还不支持此登录方式！')

        return wrapper
    return outwrapper


@login(type='qq')
def first_page(name):
    print('this is first page ',name)

@login(type='weixin')
def second_page():
    print('this is second page ')

first_page('haha')
second_page()
'''
import time
def timer(func):
    def wrapper():
        print('before time',time.time())
        func()
        print('after time',time.time())
    return wrapper

@timer
def test():
    time.sleep(1)
    print('haha')

test()