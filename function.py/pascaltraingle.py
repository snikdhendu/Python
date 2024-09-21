n=int(input("Enter no of rows:"))
list_1=[]
for i in range(n):
    temp_list=[]
    for j in range(i+1):
            if(j==0 or j==i):
                  temp_list.append(1)
            else:
                  temp_list.append(list_1[i-1][j]+list_1[i-1][j-1])

    list_1.append(temp_list)           
print(list_1)  
for i in range(n):
      for j in range(n-i-1):
            print(format(" ","<2"),end=' ')
      for j in range(i+1):
              print(format(list_1[i][j],"<5"),end=' ') 
      print()                           