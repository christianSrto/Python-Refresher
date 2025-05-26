# Membership operators = used to test if a value is in a sequence

word = "apple"

letter = "l"

if letter in word:
    print(f"{letter} is in {word}")
else:
    print(f"{letter} is not in {word}")


email = "test@gmail.com"

if "@" in email and "." in email:
    print("Valid email address")
else:
    print("Invalid email address")


even = [2, 4, 6, 8, 10]
num = 3
if num not in even:
    print("3 is not in the list of even numbers")
else:
    print("this is an eben number")
