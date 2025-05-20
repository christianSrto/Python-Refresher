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


#Logical operators = and, or, not 
#They are used to combine conditional statements

temp = 30
is_raining = False

if temp > 25 and not is_raining:
    print("It's a nice day for a walk.")
elif temp <0 and is_raining:
    print("Be careful, it's icy outside!")
elif temp < 0 or is_raining:
    print("Maybe stay indoors.")



#Conditional expressions = A one-liner if statement also known as a ternary operator

num = 5 
x = 10
y = 20

print ("Even" if num % 2 == 0 else "Odd")

max_value = x if x > y else y
print(f"The maximum value is: {max_value}")
