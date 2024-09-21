list = []
while True:
	try:
		n = int(input("Enter input: "))
	except Exception as exp:
		break
	list.append(n)
list.reverse()
print(list)

list.reverse()
print(list.pop())