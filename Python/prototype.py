from copy import deepcopy

# Prototype
class Shape:
    def __init__(self, shape_type):
        self.shape_type = shape_type

    def clone(self):
        return deepcopy(self)
    
# ConcretePrototype
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def info(self):
        return f"A {self.shape_type} of radius {self.radius}"
    
# ConcretePrototype
class Square(Shape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def info(self):
        return f"A {self.shape_type} of side {self.side}"
    

# Client code
if __name__ == '__main__':
    circle = Circle(5)
    print(circle.info())

    square = Square(4)
    print(square.info())

    another_circle = circle.clone()
    another_circle.radius = 7
    print(another_circle.info())

    another_square = square.clone()
    another_square.side = 6
    print(another_square.info())
