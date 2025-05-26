# List Comprehension = a compact way to create lists, more readable and concise than traditional for loops

# Using for loop and append method
doubles = []

for x in range(1,11):
    doubles.append(x * 2)

print(doubles)


# Using list comprehension to achieve the same result
new_doubles = [x*2 for x in range(1,11)]
print(new_doubles)


numbers = [1, -2, 3, -4, 5, -6]

positive_numbers = [num for num in numbers if num >= 0]
print(positive_numbers)