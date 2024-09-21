phone_no=dict({
    'snik': 999,
    'ankur': 100,
    'bristi': 890,
    'rahul': 789

})
# values can be anything means tuple ,list,int,dictionary
# but in case of key we can only use tuple, int , string
phone_no['snik']=9382618820
print(phone_no) #we can use this

print(phone_no.items()) #we can also we this methods

phone_no['snik']={'snik_home':98989,'snik_office':530}

print(phone_no) #we can use this
print(phone_no['snik']) #we can use this
print(phone_no['snik']['snik_home']) #we can use this

for i in phone_no:
    print(i)  #Print only the key values of the phone number
    print(phone_no[i]) #here print all values


for i in phone_no.values():
    print(i)  #Print only the key values of the phone number   

# we can copy element from one dictionary to another dictionary
dic2=phone_no.copy()
print(dic2)
print(len(dic2))