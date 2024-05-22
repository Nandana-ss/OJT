# Create a class Square that inherits from the Rectangle class. Add a method calculate_diagonal() to calculate the diagonal of the square.
import math

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def calculate_diagonal(self):
        return self.length * math.sqrt(2)

if __name__ == "__main__":
 
    sq = Square(4)

    area = sq.calculate_area()
    print(f"The area of the square is: {area}")

    perimeter = sq.calculate_perimeter()
    print(f"The perimeter of the square is: {perimeter}")

    diagonal = sq.calculate_diagonal()
    print(f"The diagonal of the square is: {diagonal:.2f}")
