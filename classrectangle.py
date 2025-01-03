class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def compare(self, other):
       return self.area() < other.area()

    def display(self):
        print(f"Length: {self.length}, breadth: {self.breadth}, Area: {self.area()}")

rect1 = Rectangle(5, 4)
rect2 = Rectangle(6, 3)

rect1.display()
rect2.display()

rect1.compare(rect2)
print("Rectangle 1 has a smaller area than Rectangle 2.")
