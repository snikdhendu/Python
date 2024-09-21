def count(s):
    up=0
    lower=0
    for i in s:
        if(i.isupper()):
            up=up+1
        else:
            lower=lower+1
    print("up:",up)
    print("low:",lower)
s=input("Enter a string:")    
count(s)
