z=input("Enter the source file name:")
n=input("Enter a string to check:")
y=open(z,'r')
x=y.readlines()
count=0
for i in x:
		# p=i
		count+=i.count(n)
print("The number of ",n,"in the string is:",count)		
