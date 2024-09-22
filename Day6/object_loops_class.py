#######################[LETS WORK WITH OBJECT]################################


#ever thing in python is object

age = 56
print(age.real)
print(age.imag)

#bit_length function is used to check how bit are used to store the varible in memory
print(age.bit_length())


items = [1,2]

items.append(3)
#result = [1,2,3]

items.pop()
#result = [1,2]
print(items)
#result = [1,2]

#we can also check the location of where the data is store with the help of

print(id(items))

#result = 1903066265408 location of the memory


age1 = 18

age1 = age1 +1

print(age1)

#######################[LETS WORK WITH LOOPS]################################
#WHILE LOOP EXAMPLE 
condition = True
while condition == True:
    print("the condition is true")
    condition = False
#result = False


#another example of while loop

count = 0
while count < 10 :
    print("the condition is true")
    count = count +1 #count += 1
print("After the loop")

#result=[
#multi line comment
"""the condition is true
#the condition is true
#the condition is true
#the condition is true
#the condition is true
#the condition is true
#the condition is true
#the condition is true
#the condition is true
#the condition is true
#the condition is true
#After the loop]"""


#FOR LOOPS IN PYTHON

boys = [1,2,3,4]

for boy in boys:
    print(boy)
#result =1 ,2,3,4

#now lets run loop in range funtion can return form starting to end value

for boy in range(15):
    print(boy)

#result =
"""1
2
3
4
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14"""

#now lets check the index of list with help of loops

"""with the help of enumerate function we can aslo return the index of list element"""
elements = [1,2,3,4,5] #its can also be name or string or anything like = ["deewakar","kishan","vadant"]
for index,element in enumerate(elements):
    print(index, element)

#result=
"""
0 1
1 2
2 3
3 4
4 5
"""


#know let work with BREAK AND CONTINUE

items = [1,2,3,4,5]
for item in items:
    if item == 2:
        continue
    print(item)

""""
1
3
4
5
"""
for item in items:
    if item == 2:
        break
    print(item)
"""
1
"""

#####################################[LETS WORK WITH CLASS IN PYHTON]############################3


class Dog:
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
#result =
"""
rocko
8
"""

"""           NOW LETS WORK WITH INHERTANCE IN CLASS WITH PYTHON               """
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
