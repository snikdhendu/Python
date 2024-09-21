# here we see that raise key word basically works let see

try :
    a=int(input("Enter your age:"))
    if(a<0):
        raise ValueError #basically we here check the value that use is given if it is less than 0 then simply raise the value error
except ValueError:
    print("sorry age should be positive")