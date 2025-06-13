# @property = Decorator used to define a method as a property, allowing it to be accessed like an attribute
#             It adds addtitional logic when read, writem or delete attributes
#             Gives you getter, settes and deleter methods

class Rectangle:
    def __init__(self, width, height):
        # underscore before the variable name indicates that it is intended to be private
        self._width = width
        self._height = height


    @property
    def width(self):
        return f"Width: {self._width:.1f}cm"
        
    @property
    def height(self):
        return f"Width: {self._height:.1f}cm"
        
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")

rectangle = Rectangle(10, 20)


#updated with setter
rectangle.width = 15
rectangle.height = 30

print(rectangle.width)
print(rectangle.height)


#deleted with deleter
del rectangle.width
del rectangle.height

