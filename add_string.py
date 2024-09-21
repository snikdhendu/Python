n=input("Enter a string : ")
mid_len=len(n)//2
new_string=input("Enter a new string : ")
print(n[:mid_len])
print(n[mid_len:])


result_string=n[:mid_len]+new_string+n[mid_len:]
print("Result string:",result_string)
