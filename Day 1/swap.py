# Write a Python program to swap two numbers without using a temporary variable.(15-05-2024)
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
print("unswapped first number: ",a)
print("unswapped second number: ",b)
a=a+b
b=a-b
a=a-b
print("swapped first number: ",a)
print("swapped second number: ",b)