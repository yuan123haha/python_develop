# Author:haha

class Animal(object):
    def __init__(self,name):
        self.name=name

    @staticmethod
    def animal_talk(obj):
        obj.talk()

class Dog(Animal):
    def talk(self):
        print('wang wang')

class Cat(Animal):
    def talk(self):
        print('miao miao')

d=Dog('haha')
d.talk()
#输出：wang wang
c=Cat('enen')
c.talk()
#输出：miao miao
Animal.animal_talk(d)
#输出：wang wang
Animal.animal_talk(c)
#输出：miao miao