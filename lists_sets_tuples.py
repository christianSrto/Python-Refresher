# Collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates are ok
# Set = {} unordered amd immutable, but Add/Remove are ok. No Duplicates
# Tuple = () ordered and unchangeable. Duplicates are ok


#Lists
print("Lists:\n")
fruits = ["apple", "orange", "banana", "mango"]

#print(help(fruits)) shows all methods 
print (fruits)
print (fruits[0:2])

print(len(fruits)) #prints the number of items in the list

print("apple"in fruits)#boolean to find a value in a list

fruits[0] = "pineapple"#reassigns a value

fruits.append("strawberry")#adds a value to the end

fruits.remove("banana")#removes the value from list

fruits.insert(0, "cherry")#adds value to the front of the list

fruits.reverse()
print (fruits)

fruits.sort()
print(fruits)

print(fruits.index("cherry"))

print(fruits.count("strawberry"))

for fruit in fruits:
    print(fruit)

fruits.clear()
print(fruits)


#Sets
print("\n\nSets:\n")
fruits = {"apple", "orange", "banana", "mango", "orange"}
print(fruits) #Sets are always in randomized order

print(len(fruits))
print("apple" in fruits)

fruits.add("pineaple")
fruits.remove("apple")
fruits.pop()
print(fruits)


#Tuples
print("\n\nTuples:\n")
fruits = ("apple", "orange", "banana", "mango", "orange")
print(fruits)
print(len(fruits))
print(fruits.index("banana"))
print(fruits.count("orange"))