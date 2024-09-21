list_1=eval(input("Enter a list:"))
n=input("Enter the file name:")
with open(n,'w') as file:
	for item in list_1:
		file.write(str(item))
print("List item written to the file successfully")		
	
