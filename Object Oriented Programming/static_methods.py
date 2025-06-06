# Static Methods = A method that belong to a ckass rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance Methods = Best for operations on instances of the class (objects)
# Static Methods = Best for utility functions that don't need access to instance or class data

class Employee:
     
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} works as a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Developer', 'Designer', 'Analyst']
        return position in valid_positions
    
employee1 = Employee('Alice', 'Developer')
employee2 = Employee('Bob', 'Manager')
employee3 = Employee('Charlie', 'Intern')

# Required to create an instance of the class to call instance methods
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())


# Static method can be called without creating an instance of the class
print(Employee.is_valid_position('Manager'))

