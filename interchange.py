n=int(input("Enter the no. of element in the list:"))
list_1=[]
for i in range (n):
	k=input("Enter:")
	list_1.append(k)
	temp_1=list_1[0]
	temp_2=list_1[-1]
	list_1[0]=temp_2
	list_1[-1]=temp_1
print("The new edited list:")		
for j in range(n):
	print(list_1[j],end=" ")
	
print()	

