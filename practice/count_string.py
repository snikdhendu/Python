x=input("Enter the file name:")
y=input("Enter the string to check:")
z=open(x,'r')
r=z.readlines()
count=0
for i in r:
    count=count+i.count(y)
print("the number of string:",count)
z.close()

