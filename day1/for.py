# Author:haha

age_of_haha=24
for count in range(5):
    age = int(input('age:'))
    if age_of_haha==age:
        print('yes,you got it.')
        break
    elif age_of_haha>age:
        print('think bigger....')
    else:
        print('think smaller....')
else:
    print('Please enter later')

