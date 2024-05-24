#Create a class called FileProcessor with methods to read data from a file, write data to a file, and append data to an existing file.

class FileProcessor:
    @staticmethod
    def read_file(file_path):
        """Reads the contents of a file and returns it as a string."""
        try:
            with open(file_path, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: The file {file_path} does not exist."
        except Exception as e:
            return f"An error occurred: {e}"
    
    @staticmethod
    def write_file(file_path, data):
        """Writes data to a file, overwriting any existing content."""
        try:
            with open(file_path, 'w') as file:
                file.write(data)
                return f"Data written to {file_path} successfully."
        except Exception as e:
            return f"An error occurred: {e}"
    
    @staticmethod
    def append_to_file(file_path, data):
        """Appends data to an existing file."""
        try:
            with open(file_path, 'a') as file:
                file.write(data)
                return f"Data appended to {file_path} successfully."
        except Exception as e:
            return f"An error occurred: {e}"

# Example usage
# Reading from a file
print(FileProcessor.read_file('example.txt'))

# Writing to a file
print(FileProcessor.write_file('example.txt', 'Hello, World!'))

# Appending to a file
print(FileProcessor.append_to_file('example.txt', '\nAppend this text.'))
