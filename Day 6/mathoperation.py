#Create a class called MathOperations with class methods for basic mathematical operations like addition, subtraction, multiplication, and a static method to find the factorial of a number. 

class MathOperations:
    @classmethod
    def addition(cls, a, b):
        return a + b
    
    @classmethod
    def subtraction(cls, a, b):
        return a - b
    
    @classmethod
    def multiplication(cls, a, b):
        return a * b
    
    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result

# Example usage
print(MathOperations.addition(3, 4))        # Output: 7
print(MathOperations.subtraction(10, 5))    # Output: 5
print(MathOperations.multiplication(6, 7))  # Output: 42
print(MathOperations.factorial(5))          # Output: 120

        
        