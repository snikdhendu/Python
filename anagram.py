a=input("Enter a string:")
b=input("Enter another string:")
if(len(a)!=len(b)):
	print("Strings are not anagram")
else:
	if(sorted(a)==sorted(b)):
		print("strings are anagram")
	else:
		print("Strings are not anagram")			
