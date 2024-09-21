def sorted_by_key(dict) :
   
    new_dic={}
    sk=sorted(dict.keys())

    for i in sk:
        new_dic[i]=dict[i]
    print(new_dic)   
def sorted_by_value(dict):
    print(sorted(dict.items(),key=lambda x:x[1]))
input_dict = {}
num_entries = int(input("Enter the number of key-value pairs: "))

for _ in range(num_entries):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    input_dict[key] = value
sorted_by_key(input_dict)
sorted_by_value(input_dict)