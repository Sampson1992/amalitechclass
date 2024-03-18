# working with strings
#print("my name is sampson")
#law = ("happy birthday my love!")
#print(len(law))
# check string in or not true or false
law = ("today, a lot people are not speaking and they risk of their stipends")
print("stipends" in law)
print("amalitech" in law)
#string concatenation
a = "beautiful"
b= "day"
c = a + " " + b
print(c)

# list
myfruits = ["apple", "banana", "date", "mango", "orange", "cherry"]
print(myfruits)
#accessing the fruits
print(myfruits[4])
# ranges of index
print(myfruits[2:])
#changes
myfruits[1]= "kiwi"
print(myfruits)
#inserting item
myfruits.insert(2, "watermelon")
print(myfruits)
# adding item to a list
myfruits.append('coconut')
print(myfruits)
# removing from a list
myfruits.remove('date')
print(myfruits)

# learning tuples now
members = ("janet", "malik", "john","albert", "pato", "ruth", "nancy", "daniel")
print(members)
# accesing the tuple items
print(members[2:5])
#adding item to a tupple
y = list(members)
y.append("samuel")
members = tuple(y)
print(members)

# dictionartionary
dic = {
    "brand": "ford",
    "model": "mustang",
    "year": 2023
}
print(dic['brand'])
#chnaging dictionary items
dic["year"] = 2024
print(dic)
#updating dic item
dic.update({"brand": "bmw"})
print(dic)
# adding itmes to dic
dic ["color"] = "red"
print(dic)



