a="1"
b=2
c=int(a) #here we convet string a as integer then add into an integer this is actually called type casting
print("The sum of the two number:",b+c)
print(int(a)+int(b))

# implicit Typecasting
a=8.8
b=1
c=a+b #here b change it's type automatically int to float
print(type(c),c)