n=[]
a=int(input("Enter the no. of elements:"))
count_even=0
count_odd=0
for i in range(a):
	k=int(input("Enter:"))
	n.append(k)
print("The inputed list",n)
for j in range(a):
	if(n[j]%2==0):
		count_even=count_even+1
	else:
		count_odd=count_odd+1		
print("The no of even no:",count_even)
print("The no of odd no:",count_odd)	
