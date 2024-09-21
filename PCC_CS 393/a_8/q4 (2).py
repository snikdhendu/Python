
z=input("Enter the source file name:")
x=open(z)
y=input("Enter file name where you want to copy the content:")
a=open(y,'w')
for i in x.readlines():
	a.write(i)
print("Content copied!!!!!!")	
