class Shape:
    def __init__(self, name):
        self._name = name  # Protected

    def get_name(self):
        return self._name

    def __display(self):
        print(f"This is a shape name: {self._name}.")

    def display_info(self):
        self.__display()


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)  
        self.__length = length  # Private
        self.__width = width    

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def display_info(self):
        super().display_info() 
        print(f"Length: {self.__length}  \nwidth: {self.__width}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")


rect = Rectangle("Rectangle", 10, 8)

rect.display_info()
