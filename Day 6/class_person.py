#Create a class called Person with attributes for name, age, and email. Implement validation to ensure that age is a positive integer and email follows a valid format.

import re

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer.")
        self._age = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, value):
            raise ValueError("Invalid email format.")
        self._email = value

# Example usage
try:
    person1 = Person("Alice", 25, "alice@example.com")
    print("Person 1 created successfully.")
except ValueError as e:
    print(e)

try:
    person2 = Person("Bob", -30, "bob@example")  # Invalid age
    print("Person 2 created successfully.")
except ValueError as e:
    print(e)

try:
    person3 = Person("Charlie", 35, "invalid-email")  # Invalid email
    print("Person 3 created successfully.")
except ValueError as e:
    print(e)
