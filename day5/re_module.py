import re

# re.split('[0-9]','abc12f3GH')
# print(re.search(r'\\','abc\d'))
print(re.search('.+','abcb\n123',flags=re.S))