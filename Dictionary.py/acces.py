info={"apple":34,"orango":36,"Mango":467,12:"Bristi",35:"saikat",'r':"rahul"}
print(info["Mango"]) #we can acess element by this keyword

print(info.get('r')) #also we can this to access the element

# To access all keys at a time we can use this
print(info.keys())
print(info.values())

# We can also this
for i in info.keys():
        print(info[i])

for i in info.keys():
        print(f"The value corresponding to the key {i} is {info[i]}")        
        

