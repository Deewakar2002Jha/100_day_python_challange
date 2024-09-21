##########################################{    HOW TO WORK WITH SETS      ]#########################

#function is set of instruction that we run when we needed it
#defining the function
# a function should be meaningfull so anybody understand what function does
def hello(name):
    #argument are the variable that we pass throught function whenwe called
    print('hello !' +name)
    #parameter are variable that we pass inside function body is function define
#sytax to call 
hello("deewakar jha")

#result = hello ! deewakar 

def callingfriend(name1 = "my friend"):
    print("hello !" +name1)

#calling the function with value so it use default value
callingfriend()
#result = hello !my friend

#and if pass a value in function then they print that value
callingfriend("kishan")
#result = hello !kishan


#we can also use multiple parameter in fucntion
def familydata(name3 , age):
    print("my name is " + name3 +"  " +" my age is " + str(age))

#calling function with default value
familydata("deewakar jha" , 22)
#result = my name is deewakar jha   my age is 22

#parameter are called by refernce

def change(value):
    value = 2
val = 1
change(val)

print(val)

#result = 1

#an example with dictionaries in function
def change2(value):
    value["name"] = "deewakar"

val = {"name":"kishan"}
change(val)

print(val)

#result ={'name': 'kishan'}

#now we learn about return statement in function

def returnfun(name3):
    print('hello' + name3 + '!')
    return name3
#this function will not reutrn any thing
def returnfun1(name4):
    if not name4:
        return
    print('hello ' + name4 + '!')
    #this will not return any thing
    

returnfun1("deewakar")

#result = hello deewakar!

#############################[LETS WORK WITH VARIABLE SCOPE ]######################

age  = 8

def test():
    print(age)

print(age) #8
test()

#############################[LETS WORK WITH NESTED FUNCTION ]######################
def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('i am going to buy the milk')

#another example of nested function
def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()
    
count()



