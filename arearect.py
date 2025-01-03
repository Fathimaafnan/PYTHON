class Rectangle:
    # Constructor to initialize the rectangle's length and width
    def __init__(self, length, width):
        self.__length = length  # Private attribute
        self.__width = width  # Private attribute

    # Method to calculate the area of the rectangle
    def area(self):
        return self.__length * self.__width

    # Overloading '<' operator to compare areas of two rectangles
    def __lt__(self, other):
        # Compare the areas of two rectangles
        return self.area() < other.area()

    # Method to display the dimensions and area of the rectangle
    def display(self):
        print(f"Length: {self.__length}, Width: {self.__width}, Area: {self.area()}")


# Creating two Rectangle objects
rect1 = Rectangle(5, 4)  # Rectangle with length 5 and width 4
rect2 = Rectangle(6, 3)  # Rectangle with length 6 and width 3

# Displaying the rectangles
rect1.display()
rect2.display()

# Comparing the two rectangles using the '<' operator
if rect1 < rect2:
    print("Rectangle 1 has a smaller area than Rectangle 2.")
else:
    print("Rectangle 1 does not have a smaller area than Rectangle 2.")
