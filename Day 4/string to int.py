# Write a Python program with a function that converts a string to an integer. Handle exceptions within the function and print appropriate error messages.
def string_to_int(string):
    try:
        return int(string)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
print(string_to_int("123"))
print(string_to_int("abc"))