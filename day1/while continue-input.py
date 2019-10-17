# Author:haha
age_of_haha=24
count=0
while count<5:
    age = int(input('age:'))
    if age_of_haha==age:
        print('yes,you got it.')
        break
    elif age_of_haha>age:
        print('think bigger....')
    else:
        print('think smaller....')
    count=count+1
    if count==5:
        continue_info=input('do you want to guessing...y/n:')
        if continue_info=='y':
            count=0
