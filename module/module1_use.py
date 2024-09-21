# import module1
# print("The sum value is:",module1.sum(10,20))
# print("The mul value is:",module1.multipy(10,20))

# we can use above technique
# or we can use below technique

import module1
from module1 import sum
print(sum(10,20))

# if we want call all function all together we can use * instead of using specific function name

# we can also rename module name 
# we can use this thing for renaming module

# import module as m
# now we can use m as module name