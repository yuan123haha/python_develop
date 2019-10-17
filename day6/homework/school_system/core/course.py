# Author:haha

class Course(object):
    def __init__(self,name,price,cycle):
        self.cycle=cycle
        self.price=price
        self.name=name
        self.class_list=[]
