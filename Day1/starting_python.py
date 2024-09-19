name = "deewakar jha"
print(name)
age = 39
print(age)
#defining the rule of variable in python
#it cannot  be start with the number and use a keyword in python
# 1234 or test@ or test! or if or else


#know we learn abbout the datatype and we can check the type of the variable by type function
print(type(name))
print(type(name) == str)#we can check our datatype by using the this that the datatype difine actull hold the same datatyle

#to check the instance of the string we use this
print(isinstance(name, str))

age = 2
print(isinstance(age,float))
age1 = 2.9
print(isinstance(age1,float))
#how can we change the datatype of variable in python using class constructer
age3 = float(2)
print(isinstance(age3,float))

#now we can also pass a varible in datatype in varible by defining it in start
number = "20"
age = int(number)
print(isinstance(age,float))#we can check it by using differnt datatype

#complex for complex number
#bool for booleans
#list for lists
#tuple for tuples
#range for ranges
#dict for dictionaries
#set for sets

########################    KNOW WE LEARN ABOUT THE OPERATER IN PYTHON   #############
1+1 #2
2-1 #1
2*2 #4
4/2 #2
4%3 #1
4**2 #16
4//2 #2

print(" Scamp " + "is a good dog")
age = 8
age += 8 #age = age+8=16

print(age)

#conparsion operater
a = 1
b = 2

a==b #false
a != b #true
a>b #false
a<=b #true

print(0 or 1) ##1
print(False or 'hey') ##hey
print('hi' or 'hey' )
print([] or False)##false
print(False or []) ##'[]'

########################    KNOW WE LEARN ABOUT THE BITWISE OPERATER IN PYTHON   #############

# & perform binary AND
# | perform binary OR
# ^ perform a binary XOR operation
# ~ perform a binary NOT operation
# << shirt left operation
# >> shirt right operation


########################    KNOW WE LEARN ABOUT THE TERNIARY OPERATER IN PYTHON   #############

#WITHOUT TERNINARY OPERATOR
def is_adult(age):
    if age > 18:
        return True
    else:
        return False

#WITH USE OF TERNINARY OPERATOR
def is_adult2(age):
    return True if age > 18 else False

########################    KNOW WE LEARN ABOUT THE STRING OPERATION IN PYTHON   #############

print("deewakar".upper())
print("KISHAN".lower())
print("hey my name is chim tap".title())
print("HSHBDJKNjjdifdn".islower() )

name = "deewakar"
print(len(name))#check the lenght of string

 

