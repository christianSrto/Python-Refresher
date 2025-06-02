# object = A bundle of related attributes and methods(functions withing an object)
# class = used to design the structure and layout of an object 


from car import Car



car1 = Car("Honda", "Civic", 2016, "black", False)
car2 = Car("Honda", "Accord", 2012, "Grey", True)

#Prints memory address 
print(car1)

#Prints specific attributes
print(car1.model)
print(car1.for_sale)
print(car2.year)


#runs methods from Car
car1.stop()
car2.drive()