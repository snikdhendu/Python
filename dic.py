n=int(input("Enter the number of students:"))
for i in range(n):
    assign=[]
    test=[]
    lab=[]
    name=input("Enter the name:")
    for i in range(4):
        a=int(input("enter assingment marks:"))
        assign.append(a)
    for j in range(2):
        t=int(input("Enter the test marks:"))
        test.append(t)
    for k in range(2):
        l=int(input("Enter the lab marks:"))
        lab.append(l)

    dict_1={}

    dict_1["name"]=name
    dict_1["assign"]=assign
    dict_1["test"]=test
    dict_1["lab"]=lab

    print(dict_1)


    avg=((sum(assign)/4)*0.1)+((sum(test)/2)*0.7)+((sum(lab)/2)*0.4)

    print("the avg marks:",avg)

    if(avg>90):
        print("Grade A")
    elif(avg>=70):
        print("Grade B")
    else :
        print("Grade C")

