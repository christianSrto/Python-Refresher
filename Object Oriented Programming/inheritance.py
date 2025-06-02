# Inheritance = Allows a class to inherit attributes and methods from anohter class
#               Helps with code reusibility and extensibility
#               Child(Parent)

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking")

    def speak(self):
        print("WOOF")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} is meowing")

    def speak(self):
        print("MEOW")


dog = Dog("Scooby")
cat = Cat("Garfield")


print(dog.name)
cat.eat()

dog.bark()
cat.meow()

dog.speak()
cat.speak()