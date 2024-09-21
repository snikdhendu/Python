def i (a,b,c):
    maximum=0
    # if(a>b):
    #     if(a>c):
    #         max=a
    # elif(b>a and b>c):
    #     max=b       
    # else:
    #     max=c
    maximum=max(a,max(b,c))
    return maximum

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))     
c=int(input("Enter third number:"))  
max=i(a,b,c)
print("highest number of this three number:",max)