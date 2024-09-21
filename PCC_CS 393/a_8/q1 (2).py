n=input("Enter the file name:")
f=open(n,'r')
p=int(input("Enter lines want to read:"))
y=f.readlines()
for i in range(0,7):
	print(y[i].rstrip())
f.close()		


