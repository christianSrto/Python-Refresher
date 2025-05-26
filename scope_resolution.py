# variable scope = wher a variable is accessible and visible
# scope resolution = (LEGB) = local, enclosing, global, built-in

def func1():
    a = 1 # a is a local variable to func1
    print(a)

def func2():
    b = 2 # b is a local variable to func2
    print(b)

func1()
func2()



def enclosed_func():
    x = 1 # x is a variable in the enclosing scope
    def inner_func():
        print(x)  # this x is from the enclosed scope
    inner_func()

enclosed_func()


# Global variable
x_global = 10  

def global_func():
    print(x_global)  

global_func()



# Built-in variable
from math import pi

def built_in_func():
    print(pi)

built_in_func()

