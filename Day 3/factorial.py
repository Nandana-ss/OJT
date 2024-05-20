# Write a Python program to calculate the factorial of a number using a lambda function and reduce function.
from functools import reduce
num = int(input("Enter a number: "))
factorial = reduce(lambda x, y: x * y, range(1, num + 1))
print("The factorial of", num, "is", factorial)
