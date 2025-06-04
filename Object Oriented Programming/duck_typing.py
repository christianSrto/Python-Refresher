# Duck Typing = Another way to achieve polymorphism besides inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck, then it is a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print ("Woof!")

class Cat(Animal):
    def speak(self):
        print ("Meow!")


class Car:
    # Does not inherit from animal class, but has all the necessary attributes/methods
    alive = False

    def speak(self):
        print ("Beep!")


animals = [Dog(), Cat(), Car()]


for animal in animals:
    animal.speak()
    print(f"alive = {animal.alive}")