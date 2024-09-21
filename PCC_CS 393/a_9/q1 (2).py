import random
import string
def random_string(length):
	strings=string.ascii_letters
	return (''.join(random.choice(strings) for i in range(length)))
	
def random_value(a,b):
	return(random.randint(a,b))
	
def random_multiple():
	return(random.randint(0,10)*7)
p=int(input("Enter the random string length:"))
print("The random string is:",random_string(p))
q=int(input("Enter lower bound:"))
r=int(input("Enter upper bound:"))
print("print the random value:",random_value(q,r))
print("The random multiple of 7 is:",random_multiple())
		
