########################################### HOW TO TAKE USER INPUT      ]#################################
age =input("what is you age\n")
print("your age is  " +" " + age)



########################################### HOW TO WORK WITH CONTROL STATEMENTS     ]#################################

condition = False#false the it print the else part

if condition == True:
    print("the condition")
    print("was true")
else:
    print("the condition")
    print("was False\n\n")

#ANOTHER EXAMPLE

condition = False
name = input("plase enter your name to enter")

if condition == True:
    print("the condition")
    print("was true")
elif name == "roger" :
    print("Hello Roger")
elif name == "deewakar":
    print("hello deewakar jha")
elif name == "kishan":
    print(" hello kishan")
else:
    print("welcome to condition statment")

########################################### HOW TO WORK WITH LIST      ]#################################

#list is collect of unique and diffrent element and it also allow to reference differnt element with single name
dogs = ["mia",1,"rocko","MOTI",True]
#know we use in function check a element in list or not
print("mia" in dogs)
#result= true

print("monkey" in dogs)
#result = false

#we can also add value in list

print(dogs.append("peacock"))
#result = ['mia', 1, 'rocko', 'MOTI', True, 'peacock']
print(dogs)
#we can also add value in list with index number

dogs[4]="mukesh"

print(dogs)
#we can also upadate the list
dogs[3] = "football"
#result = 
print(dogs)
#we can start with any index number in list
print(dogs[2:5])
#result = ['rocko', 'football', 'mukesh']
print(dogs[:3])
#result = ['mia', 1, 'rocko']
#we can also check the length of the list by using len function
print(len(dogs))
#result = 6

#we can also use extend method to add to list
dogs.extend(["kishan","deewakar"])
#result = ['mia', 1, 'rocko', 'football', 'mukesh', 'peacock', 'kishan', 'deewakar']
#same thing but differnt way
dogs += ["vadent","vedu"]
#result = ['mia', 1, 'rocko', 'football', 'mukesh', 'peacock', 'kishan', 'deewakar', 'vadent', 'vedu']


print(dogs)

#we can also remove element with remove function
dogs.remove("vedu")
#result = ['mia', 1, 'rocko', 'football', 'mukesh', 'peacock', 'kishan', 'deewakar', 'vadent',]

#POP method will remove on item from the list and return to the list
print(dogs.pop())

#result = vadent

print(dogs)
#result = ['mia', 1, 'rocko', 'football', 'mukesh', 'peacock', 'kishan', 'deewakar']

# how we add at a specfic value at index in list

dogs.insert(4, "moroco")
#result = ['mia', 1, 'rocko', 'football', 'moroco', 'mukesh', 'peacock', 'kishan', 'deewakar']
print(dogs)
