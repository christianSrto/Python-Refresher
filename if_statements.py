age = int (input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 65:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


name = input("Enter your name: ")
if name == "":
    print("You did not enter a name.")
else:
    print("Hello, " + name + "!")


for_sale = True
if for_sale:
    print("The item is for sale.")
else:
    print("The item is not for sale.")
