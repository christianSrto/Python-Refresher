# dictionary = a collection of {key:value} pairs ordered and changeable. No duplicates

capitals = {"Canada": "Quebec",
            "USA": "Washington D.C", 
            "India": "New Delhi", 
            "China": "Beijing", 
            "Russia": "Moscow"}

print(capitals.get("Canada"))

capitals.update({"Germant": "Berlin"})#can be used to update existing items or add an item
print(capitals)

capitals.pop("USA")
print(capitals)

capitals.popitem()#Removes latest item
print(capitals)

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)


values = capitals.values()
print(values)

for value in capitals.values():
    print(value)


items = capitals.items() #returns dictionary object that resembles a 2D List of tuples
print(items) 

for key,value in capitals.items():
    print(f"{key}: {value}")