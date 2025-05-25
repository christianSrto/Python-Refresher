#function = A block of reusable code 
#           use function() to invoke the function

def counter(count): 
    for i in range (count+1):
        print(i)

def happy_birthday(x,y):
    print(f"Happy Birthday {x}")
    print(f"You are {y} years old")

counter(2)
counter(7)

happy_birthday("Bob", 20)
happy_birthday("Jim", 34)


# return = statement used to end a function and send a result back to the caller

def add(x,y):
    z = x + y
    return z

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


print(add(4,5))
print(add(6,7))

full_name = create_name("spongebob","squarepants")
print(full_name)