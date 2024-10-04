#Lists : ordered ,mutable,allow duplicate elements

mylist = ["banana","cherry","apple"]

print(mylist)
#accesing the element in list
item = mylist[0]

print(item)
#result = banana

#to print list in iteration using for loop
for i in mylist:
        print(i)
"""
banana
cherry
apple
"""


#to check item in list or not we check through in operator

if "banana" in mylist:
    print("yes")
else:
    print("no")
#result=yes


#to check mu element in list with length function

print(len(mylist))
#Result = 3

#we can also add element in list with the hepl of append function
mylist.append("lemon")
print(mylist)
#result =["banana","cherry","apple","lemon"]

#we can aslo insert item at any index in list
"""
syntax:-listname.insert(index,value)
"""
mylist.insert(1,"blueberry")
print(mylist)
#result= ["banana","blueberry","cherry","apple","lemon"]

#we can aslo remove item with the help of pop function
item = mylist.pop()

print(item)
print(mylist)
#result=["banana","blueberry","cherry","apple"]
