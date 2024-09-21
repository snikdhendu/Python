n=[]
a=int(input("Enter the no. of elements:"))
count_pos=0
count_neg=0
for i in range(a):
	k=int(input("Enter:"))
	n.append(k)
print("The inputed list:",n)
for j in range(a):
	if(n[j]>0):
		count_pos=count_pos+1
	else:
		count_neg=count_neg+1		
print("The no of positive no:",count_pos)
print("The no of negative no:",count_neg)
