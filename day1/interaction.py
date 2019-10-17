# Author:haha
name=input('name:')
age=int(input('age:'))
print(type(age),type(str(age)))
job=input('job:')
salary=input('salary:')
info3='''
----info of haha---
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)
print(info3)