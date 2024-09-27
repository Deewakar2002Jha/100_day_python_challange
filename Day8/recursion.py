#Recursion

def factorial(n):
    if n == 1:return 1
    return n * factorial(n-1)

print(factorial(3))

#rsult=6

def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

#decorators
@logtime
def hello():
    print("hello")

hello()

"""result = before
            hello
            after"""

#Decstrings
def increment(n):
    """Increment a number"""
    return n+1


class Dog:
    """A class representing a dog"""
    def __init__(self,name,age):
        """initialize a new dog"""
        self.name = name
        self.age = age

    def bark(self):
        """"let the dog bark"""
        print('WOF!')
print(help(Dog))


#Annotation
def increment(n:int) -> int:
    return n+1

count:int = 0

#Exceptions

"""
try:
    #some lines of code
except<ERROR!>:
    #handler <error!>
except<error2>:
    #handler <error2>
except:

else:
    #no exception were raised , the code raan successfully
finally:
    #do something in any case
"""
try:
    result = 2 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    result = 1
print(result) #1

try:
    raise Exception('an error')
except Exception as error:
    print(error)
    

class DogNotFoundException(Exception):
    print("inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print('Dog not found!')

#working with statement in python
filename = '/Users/flavio/rest.txt'
"""without with statement"""
try:
    file = open(filename, 'r')
    content = file.read()
    print(content)
finally:
    file.close()
"""with with statement"""
filename= '/Users/flavio/test.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content)
