#Lists : ordered ,mutable,allow duplicate elements

mylist = ["banana","cherry","apple"]

print(mylist)
#accesing the element in list
item = mylist[0]

print(item)

#to print list in iteration using for loop
for i in mylist:
        print(i)


#to check item in list or not we check through in operator

if "banana" in mylist:
    print("yes")
else:
    print("no")
