# Write a Python program to print the multiplication table of a number using a for loop.(15-05-2024)
a=int(input("enter the first number: "))
if a>0:
    for i in range(1,13):
      c=a*i
      print(a,"*",i ,"=" ,a*i)
else:
    print("the number should be positive")