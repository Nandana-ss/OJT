# Write a Python program to create a class called Rectangle. The class should have attributes length and width, and methods calculate_area() to calculate the area of the rectangle and calculate_perimeter() to calculate the perimeter.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


if __name__ == "__main__":
    
    rect = Rectangle(5, 3)

    area = rect.calculate_area()
    print(f"The area of the rectangle is: {area}")
    
    perimeter = rect.calculate_perimeter()
    print(f"The perimeter of the rectangle is: {perimeter}")


