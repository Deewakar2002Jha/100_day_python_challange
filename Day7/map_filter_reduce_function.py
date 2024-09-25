python
import argparse

# Create an ArgumentParser object to parse command line arguments
parser = argparse.ArgumentParser(
    description='this program print the name of my dogs'
)
# Add a required argument '-c' or '--color' to search for a specific color
parser.add_argument('-c','--color',metavar='color',required= True, help='the color to search for')

# Parse the command line arguments
args = parser.parse_args()

# Print the color argument passed
print(args.color)

# Define a lambda function that takes a number and returns its double
lambda num : num *2

# Define a lambda function that takes two numbers and returns their product
multiple = lambda a,b : a * b

# Test the multiple lambda function with arguments 2 and 4
print(multiple(2,4))

#########################################[LETS WORK WITH MAP , FILTER, REDUCE FUNCTION]#################################################33

# Define a list of numbers
number = [1,2,3]

# Define a function that takes a number and returns its double
def double(a):
    return a * 2

# Use the map function to apply the double function to each number in the list
result = map(double , number)

# Print the result (which is a map object)
print(result)
#result =<map object at 0x000001D9F94CF4C0>

# Convert the map object to a list and print it
print(list(result))
#result = [2,4,6]

# Define a lambda function that takes a number and returns its double
double = lambda a : a * 2

# Use the map function with the lambda function
result1 = map(lambda a : a * 2, number)

# Print the result (which is a map object)
print(list(result1))

# Define a list of numbers
numberlist = [1,2,3,4,5]

# Define a function that checks if a number is even
def isEven(n):
    return n % 2 == 0

# Use the filter function to filter out even numbers from the list
result2 = filter(isEven , numberlist)

# Print the result (which is a filter object)
print(list(result2))
#result = [2,4]

# Import the reduce function from the functools module
from functools import reduce

# Define a list of expenses
expenses = [
        ('Dinner' ,80),
        ('car repair',120)
    ]

# Use the reduce function to calculate the total expense
sum = reduce(lambda a, b:a[1] + b[1], expenses)

# Print the total expense
print(sum)

 
import argparse

# Create an ArgumentParser object to parse command line arguments
parser = argparse.ArgumentParser(
    description='this program print the name of my dogs'
)
# Add a required argument '-c' or '--color' to search for a specific color
parser.add_argument('-c','--color',metavar='color',required= True, help='the color to search for')

# Parse the command line arguments
args = parser.parse_args()

# Print the color argument passed
print(args.color)

# Define a lambda function that takes a number and returns its double
lambda num : num *2

# Define a lambda function that takes two numbers and returns their product
multiple = lambda a,b : a * b

# Test the multiple lambda function with arguments 2 and 4
print(multiple(2,4))

#########################################[LETS WORK WITH MAP , FILTER, REDUCE FUNCTION]#################################################33

# Define a list of numbers
number = [1,2,3]

# Define a function that takes a number and returns its double
def double(a):
    return a * 2

# Use the map function to apply the double function to each number in the list
result = map(double , number)

# Print the result (which is a map object)
print(result)
#result =<map object at 0x000001D9F94CF4C0>

# Convert the map object to a list and print it
print(list(result))
#result = [2,4,6]

# Define a lambda function that takes a number and returns its double
double = lambda a : a * 2

# Use the map function with the lambda function
result1 = map(lambda a : a * 2, number)

# Print the result (which is a map object)
print(list(result1))

# Define a list of numbers
numberlist = [1,2,3,4,5]

# Define a function that checks if a number is even
def isEven(n):
    return n % 2 == 0

# Use the filter function to filter out even numbers from the list
result2 = filter(isEven , numberlist)

# Print the result (which is a filter object)
print(list(result2))
#result =