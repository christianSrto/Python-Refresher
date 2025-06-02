# Multiple Inheritance = inherit from more than one parent class
#                        C(A, B)
# Multilevel Inheritance = inherit from a parent which inherits from another parent class
#                        C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")


#Inherits from Animal class
class Prey(Animal): 
    def flee(self):
        print(f"{self.name} is fleeing!")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting!")


# Inherits from Prey class
class Rabbit(Prey):
    pass

# Inherits from Predator class
class Hawk(Predator):
    pass

# Inherits from both Prey and Predator classes
class Fish(Prey, Predator):
    pass



rabbit = Rabbit("Bugs Bunny")
hawk = Hawk("Tony")
fish = Fish("Nemo")


rabbit.flee()
hawk.hunt()

#Has access to both methods from the different parent classes
fish.flee()
fish.hunt()
fish.eat()


rabbit.eat()
hawk.eat()

