def mul(li):
    mul=1
    for i in li:
        mul=mul*i
    return mul
# list_1=map(int,input("Enter list element :").split(","))  
list_1=[]
n=int(input("enter number  of elements:"))
for j in range(n):
    k=int(input("Enter:"))
    list_1.append(k)
print("Final list:",list_1)    
p=mul(list_1)
print("The mulpication of the list elements:",p)


    