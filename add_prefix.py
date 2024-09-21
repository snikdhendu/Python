n=input("Enter a string: ")
p=n.split() #basically here split create a list for storing the value of the each string
print(p)
a=input("Enter a prefix:")
q=''
for i in range(len(p)):
	q += a + p[i]
	q+=" "
print(q)

