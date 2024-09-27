# Recursion
def factorial(n):
    # Base case: if n is 1, return 1
    if n == 1:
        return 1
    # Recursive case: return n multiplied by the factorial of n-1
    return n * factorial(n-1)

print(factorial(3))  # Result: 6

# Decorators
def logtime(func):
    # Define a wrapper function that logs the time
    def wrapper():
        # Print "before" before calling the function
        print("before")
        # Call the function and store the result
        val = func()
        # Print "after" after calling the function
        print("after")
        # Return the result
        return val
    # Return the wrapper function
    return wrapper

# Apply the logtime decorator to the hello function
@logtime
def hello():
    # Print "hello"
    print("hello")

hello()
# Result:
# before
# hello
# after

# Docstrings
def increment(n):
    """Increment a number by 1"""
    return n + 1

class Dog:
    """A class representing a dog"""
    def __init__(self, name, age):
        """Initialize a new dog with a name and age"""
        self.name = name
        self.age = age

    def bark(self):
        """Let the dog bark"""
        print('WOF!')

print(help(Dog))

# Annotations
def increment(n: int) -> int:
    """Increment a number by 1"""
    return n + 1

count: int = 0

# Exceptions
try:
    # Try to divide 2 by 0
    result = 2 / 0
except ZeroDivisionError:
    # Catch the ZeroDivisionError and print an error message
    print("Cannot divide by zero!")
finally:
    # Set result to 1 in any case
    result = 1
print(result)  # Result: 1

try:
    # Raise an Exception with a custom error message
    raise Exception('an error')
except Exception as error:
    # Catch the Exception and print the error message
    print(error)

class DogNotFoundException(Exception):
    # Define a custom Exception class
    pass

try:
    # Raise the custom Exception
    raise DogNotFoundException()
except DogNotFoundException:
    # Catch the custom Exception and print an error message
    print('Dog not found!')

# Working with statements in Python
filename = '/Users/flavio/rest.txt'

# Without with statement
try:
    # Open the file in read mode
    file = open(filename, 'r')
    # Read the file content
    content = file.read()
    # Print the file content
    print(content)
finally:
    # Close the file in any case
    file.close()

# With with statement
filename = '/Users/flavio/test.txt'

with open(filename, 'r') as file:
    # Read the file content
    content = file.read()
    # Print the file content
    print(content)