

tuplename = ("kishan","deewakar")

tuplename[0]

tuplename.index("kishan")

#we can also count the element in tuple with lenght function
print(len(tuplename))
#result = 2

#we can also check the elememt in tuple is occur or not

print("kishan" in tuplename)

#result = true

#we can also add the name of exiting tuple to new tuple
newtuple = tuplename + ("vadant" , "shivam")

print(newtuple)

#result = ('kishan', 'deewakar', 'vadant', 'shivam')


###########################################{    HOW TO WORK WITH DICTIONARIES      ]#################################
#dictionnaries is collection of element in form of key and value pair form
persondata = {"name" : "deewakar","age" : "22" , "gender" : "male" ,"state" : "bihar"}

print(persondata)
#result = {"name" : "deewakar","age" : "22" , "gender" : "male" ,"state" : "bihar"}

#we can also came the elment in dictionaries use they key name only lik

persondata["state"] = "gujarat"
#result = {'name': 'deewakar', 'age': '22', 'gender': 'male', 'state': 'gujarat'}
print(persondata)

#we can aslo get a specfic element in dic using get method

print(persondata.get("name"))
#result = deewakar

#if get method didnot find the element in dic then it can also print nane
print(persondata.get("collage"))
#result = none

#we also set default value in element if it not find in dictionaries
print(persondata.get("collage" , "ampics"))
#result = ampics

#we can also remove element form the dictionaries with the help of pop method in python with key

#persondata = {"name" : "deewakar","age" : "22" , "gender" : "male" ,"state" : "bihar"}
print(persondata.pop("gender"))
#result = male
print(persondata)
#result = {"name" : "deewakar","age" : "22" ,"state" : "bihar"}


#we the of popitem method we can get last key value in dictionaries of persondata
print(persondata.popitem())
#result  = ('state' : 'bihar')

print(persondata)
#result = {'name': 'deewakar', 'age': '22'}
