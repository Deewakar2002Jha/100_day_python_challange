"""
    LET'S LEARN ABOUT POLYMORPHISM
"""

# Polymorphism is the ability of an object to take on multiple forms.
# In this example, we have two classes: Dog and Cat.
# Both classes have an `eat` method, but they behave differently.

class Dog:
    def eat(self):
        # When a Dog object calls the `eat` method, it prints "eating dog food".
        print('eating dog food')

class Cat:
    def eat(self):
        # When a Cat object calls the `eat` method, it prints "eating cat food".
        print('eating cat food')

# We create two objects: an instance of Dog and an instance of Cat.
animal1 = Dog()
animal2 = Cat()

# When we call the `eat` method on each object, it behaves differently.
animal1.eat()  # Output: eating dog food
animal2.eat()  # Output: eating cat food

"""
    LET'S LEARN ABOUT OPERATOR OVERLOADING
"""

# Operator overloading is a feature in Python that allows us to redefine the behavior of operators like `+`, `-`, `*`, etc.
# In this example, we'll overload the `>` operator to compare the ages of two Dogone objects.

class Dogone:
    # The Dogone class has two attributes: `name` and `age`.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # We define a special method `__gt__` to overload the `>` operator.
    def __gt__(self, other):
        # When we use the `>` operator, Python calls this method.
        # It returns `True` if the age of the current object is greater than the age of the other object.
        return True if self.age > other.age else False

# We create two Dogone objects: Roger and Syd.
roger = Dogone('Roger', 36)
syd = Dogone('syd', 32)

# When we use the `>` operator, Python calls the `__gt__` method.
print(roger > syd)  # Output: True

#result=True

"""
OTHER OPERATOR
__add__() respond to the + operator
__sub__() respond to the - operator
__mul__() respond to the * operator
__truediv__() respond to the / operator
__floordiv__() respond to the //operator
__mod__() respond to the % operator
__pow__() respond to the ** operator
__rshift__() respond to the >> operator
__lshift__() respond to the << operator
__and__() respond to the & operator
__or__() respond to the | operator
__xor__() respond to the ^ operator

"""
