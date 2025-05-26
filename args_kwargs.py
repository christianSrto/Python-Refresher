# *args = allows you to pass multiple non-keyword arguments to a function
# **kwargs = allows you to pass multiple keyword arguments to a function

#args is a tuple
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 5))  


def display_name(*args):
    for name in args:
        print(name, end = " ")

display_name("Spongebob", "Squarepants")


#kwargs is a dictionary
def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")

print_address(street= "123 Dundas St", city= "Toronto", province= "ON", zip="ABC 123")



