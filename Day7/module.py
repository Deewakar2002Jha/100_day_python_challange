class Animal:
    #defing the function
    def walk(self):
        print("walking ...")
        
class Dog(Animal):
    #now lets create constructer
    def __init__(self, name,age):
            self.name = name
            self.age = age
    #defining method
    def bark(self):
        print("woof!")

rocko = Dog("rocko" ,8)

print(type(rocko))
#result = <class '__main__.Dog'>
print(rocko.name)
print(rocko.age)

rocko.walk()