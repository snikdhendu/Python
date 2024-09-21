# def swap(t1,t2):
#     t1,t2=t2,t1
#     return t1,t2
# tuple1=(1,2,3)
# tuple2=(4,5,6)
# print("original tuple1",tuple1)
# print("original tuple2",tuple2)
# tuple1,tuple2=swap(tuple1,tuple2)
# print("edited tuple1",tuple1)
# print("edited tuple2",tuple2)


tuple_1=eval(input("Enter 1:"))
tuple_2=eval(input("Enter 2:"))

tuple_1=list(tuple_1)
tuple_2=list(tuple_2)
list_1=[]

for i in range (len(tuple_1)):
    m=tuple_1[i]%tuple_2[i]
    list_1.append(m)

new_tuple=tuple(list_1)
print("the new tuple:",new_tuple)