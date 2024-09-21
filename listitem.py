main_list = eval(input("Enter a list:"))
list_str = []
list_int = []
list_float = []

for item in main_list:
    if type(item) == str:
        list_str.append(item)
    elif type(item) == int:
        list_int.append(item)
    elif type(item) == float:
        list_float.append(item)

print("The string list:", list_str)
print("The sorted string list:",sorted(list_str))
print("The integer list:", list_int)
print("The sorted string list:",sorted(list_int))
print("The float list:", list_float)
print("The sorted string list:",sorted(list_float))

       


