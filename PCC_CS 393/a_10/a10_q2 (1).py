food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]

fifth = []

for x in food:
	try:
		fifth.append(x[10])
	except IndexError as er:
		print(er)
print(fifth)	
