

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

#we can also check that a element in the dictionaries or not with help of in operater
print("state" in persondata)
#result = False

#we can also check the keys of the dictionaries
print(persondata.keys())
#result = dict_keys(['name', 'age'])


#we can also see the dictionaries in form of list
print(list(persondata.keys()))
#result = ['name','age']

#we cna also do the same things with values
print(persondata.values())

#result = dict_values(['deewakar', '22'])

#we can also see the dictionaries in form of list

print(list(persondata.values()))

#result = ['deewakar','22']

#we can also print items in list
print(list(persondata.items()))

#result = [('name', 'deewakar'), ('age', '22')]

#we can also use len function to check lenght of the dictionaries

print(len(persondata))

#result = 2


###########################################{    HOW TO WORK WITH SETS      ]#################################

set1 = {"deewakr","kishan","vedant"}
set2 = {"kishan"}
#we can also intersection to find the comman element in sets
intersect  = set1 & set2
print(intersect)

#result = {'kishan'}

#we can also intersection to find the union of the sets

set3 = {"sherya","yashvi","vadhi" ,"angle priya","kishan"}

union  = set1 | set3
print(union)

#result = {'deewakar', 'kishan','vedant','sherya','yashvi','vidhi','angle priya'}

#we can also check the diffence between to sets using - operater

diffence = set1 - set3
print(diffence)

#result = {'deewakar' , 'vedant'}

#we can check the set is superset of other or not
superset = set1 > set3

print(superset)

#result = false

superset1 = set1 < set2

print(superset1)

#result = 



 




