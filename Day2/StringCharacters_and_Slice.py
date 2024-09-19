###########################StringCharacters_and_Slice######################
#note:-String is always false in it empty 
name="deewakar jha"

#this will only print the char of index value 1
print(name[1])
#result=e

name1 = "deewakar jha"

#this will only print the char that start with  index value one and end with index value 4 but not includen 4

print(name1[1:4])
#result=eew


name2="deewakar kumar"

#this will start from the begnning and end at the index value of 7 but not include 7
print(name[:7])
#result=deewaka


name3="kishan karmur"
#this will start with the index value 5 and were the string end
print(name3[5:])
#result=n karmur

#note [ any ] is gobal variable in python that work with the boolean

book_1_read = True
book_2_read = False
#[any] function return true if any one of the value is true
read_any_book = any([book_1_read, book_2_read])

print(read_any_book)
#result=True

ingredient_purchased = True
meal_cooked = False
#[all] is return true if all the values are true and if any one of the false then it return false
ready_to_serve = all([ingredient_purchased, meal_cooked])

print(ready_to_serve)
#result=false

##############################COMPLEX NUMBER OPERATION######################################
number1 = 2+3j
number2 = complex(2,3)
#this function will ahelp us to print imagnary and real number differently
print(number2.real,number2.imag)
#result = 2.0 3.0
 
#########################[PRE-BULIT FUNCTION]#############################################

number=-41859.5893
#abs function will covert the number into the absolute value 
print(abs(number));
#result=41859.5893

number2=5.5
#this function will return a rounded value like 5.5 convert into 6 or it point greater the 5 and it incrase the whole number and if less it decreae the number

