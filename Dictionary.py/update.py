ep1={'snik':7,'prama':90}

ep2={'anik':700,'rama':9,'rimjim':'3456'}

ep1.update(ep2)
print(ep1)

ep1.pop("rama") # we can use pop operation to delete item from the dictionary
ep1.popitem() #to delete last most element we can use this
print(ep1)
#we can use del keyword to delete the element
del ep1['anik']
print(ep1)
