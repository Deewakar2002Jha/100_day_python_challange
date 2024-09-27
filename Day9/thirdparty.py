# Working with Third-Party Packages

# PyPI (Python Package Index) is the official repository of Python packages.
# We can install packages using pip, the package installer for Python.

# Installing the requests package
# pip install requests

# Updating the package
# pip install -U requests

# Uninstalling the package
# pip uninstall requests

# Getting information about the package
# pip show requests

# List Comprehension

# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Squaring each number using list comprehension
numbers_power_2 = [n**2 for n in numbers]
print(numbers_power_2)  # Output: [1, 4, 9, 16, 25]

# Squaring each number using a for loop
numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2)
print(numbers_power_2)  # Output: [1, 4, 9, 16, 25]

# Squaring each number using the map function
numbers_power_2 = list(map(lambda n: n**2, numbers))
print(numbers_power_2)  # Output: [1, 4, 9, 16, 25]