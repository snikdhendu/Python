(a,b) = (6,0)
try:# simple use of try-except block for handling errors
    g = a/b
    print(g)
except ZeroDivisionError:
    print ("This is a DIVIDED BY ZERO error")


    # also we can use else condition with try and except
(a,b) = (6,0)
try:
    g = a/b
except ZeroDivisionError as s:
    k = s
    print (k)   
else :
    print('ha ha ')