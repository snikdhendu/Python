n=input("Enter the file name:")
f=open(n,'r')
x=f.readlines()
print("The number of lines in the file:",len(x))
f.close()












