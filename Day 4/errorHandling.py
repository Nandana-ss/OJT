# Write a Python program that reads a file and prints its content. Handle ‘FileNotFoundError’ and ‘PermissionError’ exceptions.
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PermissionError:
        print(f"You don't have permission to read file '{filename}'.")  
read_file("dummy.txt")