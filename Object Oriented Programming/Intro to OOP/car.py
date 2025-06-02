class Car:

    def __init__(self, make, model, year, colour, for_sale):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print(f"You are driving the {self.make} {self.model}")

    def stop(self):
        print(f"you are stopping the {self.make} {self.model}")