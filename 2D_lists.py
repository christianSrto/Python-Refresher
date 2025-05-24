
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "beef", "fish"]

groceries = [fruits, vegetables, meats]

print(groceries) 
print(groceries[0]) 
print(groceries[0][2])

#Prints rows of the lists within the 2D List
for collection in groceries:
    print(collection)

#Prints elements individually
for collection in groceries:
    for food in collection:
        print(food, end =" ")
    print()