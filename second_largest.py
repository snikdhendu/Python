a=[]
n=int(input("No of element:"))
for i in range(n):
	x=int(input("Enter:"))
	a.append(x)
print("The inputed list:",a)
a = a.sort()
b=a[-2]
print("The second largest element is :",b)

