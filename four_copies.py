n=input("enter a string:")
if(len(n)<2):
	print("Operation not possible")
b=n[-2:]
print(b)
b=b*4
print("the 4 copies of the last two element:",b)	
