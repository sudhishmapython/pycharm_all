




# dict() Constructor
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)
# a=dict([("a","b"),(1, 2), (3, 4)])
# print(a)


# Access Dictionary Items


# print(thisdict.items())

# 2
# for key,value in thisdict.items():
#     if value == "red":
#          print(key)

# get keys
# x = thisdict.keys()
# print(x)


# get values
# x = thisdict.values()
# print(x)

# get all items
# x = thisdict.items()
# print(x)

# Change Dictionary Items
# thisdict =	{"brand": "Ford","color": "red","year": 1961 }
# thisdict["price"] = 200000
# print(thisdict)

# Update Dictionary using update method
#
# thisdict =	{"brand": "Ford","color": "red","year": 1961 }
# # #
# thisdict.update({"price": "2000"})
# print(thisdict)
# #

# Adding Items
# thisdict ={"name":"futura","place":"calicut"}
# thisdict["prize"] = 100000
# print(thisdict)

# adding item using update method()

# thisdict = {"brand": "Ford","year": 1964}
# b={"model": "india"}
# thisdict.update(b)
# print(thisdict)

# Removing Items
# 1. pop()
car =	{
  "brand": "Ford",
  "color": "red",
  "year": 1961
}

# car.pop("color")
# print(car)

# 2.popitem()
# car.popitem()
# print(car)

# 3.del()
# del car["color"]
# print(car)




# 4. clear()
# car.clear()
# print(car)


# Copy a Dictionary
# 1. copy()

# mydict = car.copy()
# print(mydict)
# print(car)
# 2. dict()
# mydict = dict(thisdict)
# print(mydict)
# d1 = {"a": 1, "b": 2}
# d2 = {"c": 3, "d": 4,"a":90}
#
# print(d1 | d2)

# d1.update(d2)
#
# print(d1)

# nested dictionary
#
# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Tobias",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2011
#   }
# }
# myfamily["child2"]["name"]="abc"
#
# print(myfamily)





# print(myfamily["child2"]["name"])
# print(myfamily["child2"]["year"])





# dict task

# fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# mydict = {}
#
# for i in fruits:
#     if i in mydict:
#         mydict[i] += 1
#     else:
#         mydict[i] = 1
#
# print(mydict)



# s = "banana"
# char_count = {}  # empty dictionary
#
# for char in s:
#     if char in char_count:
#         char_count[char] += 1  # increment count
#     else:
#         char_count[char] = 1   # first occurrence
#
# print(char_count)



# student = {"name": "Arun", "age": 20}
# print(student.get("age"))


# student = {"mark": 20}
# student.setdefault("age", 25)
# print(student)


# d1 = {"a": 1, "b": 2}
# d2 = {"b": 3, "c": 4}
#
# print(d1.keys() & d2.keys())