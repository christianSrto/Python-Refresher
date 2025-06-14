#Decorator = A function that extends the behavior of another function
#            without modifying the base function
#            Pass the base function as an argument to the decorator 

def add_sprinkles(func):
    #without wrapper this function will always be called
    def wrapper(*args, **kwargs):
        print("You add Sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper


@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    print(f"Here is your {flavour} ice cream")


get_ice_cream("Vanilla")
