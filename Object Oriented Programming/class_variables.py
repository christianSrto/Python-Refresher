# class variables = Shared among all instances of a class 
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class Student:

    school = "Bikini Bottom University"
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1



student1 = Student("Spongebob", 25)
student2 = Student("Patrick", 20)
student3 = Student("Squidward", 30)


print(student1.name)
print(student2.name)

#Class variables are the same across different objects
print(student1.school)
print(student2.school)

#It is good practice to access class variables by the class name
print(Student.school)
print(Student.num_students)