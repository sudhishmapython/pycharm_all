

# declaration
# set1={"apple","banana","cherry","cherry",5}
# print(set1)



# set2={"apple","banana","cherry","pappaya",3,7,3}
# print(set2)

# True and 1 is considered the same value:
set2={"apple","banana","cherry",True,3,7,1}
# print(set2)

# set() Constructor
# set1=set(("apple","banana","cherry",5,5))
# print(set1)

# access items
# set1 = {"apple", "banana", "cherry"}
# for x in set1:
#     print(x)

# add item
# 1.add()
# x = {"apple", "banana", "cherry"}
# x.add("orange")
# print(x)

# 2.update()
# x = {"apple", "banana", "cherry"}
# y = {"pineapple", "mango", "cherry"}
# y.update(x)
# print(y)
# or
# x = {"apple", "banana", "cherry"}
# y = ("kiwi", "orange")
# x.update(y)
# print(x)

# remove item
# 1.remove()
# x = {"apple", "banana", "cherry",10}
# x.remove("xyz")
# print(x)

# 2.discard()
# x = {"apple", "banana", "cherry","grape"}
# x.discard("xyz")
# print(x)

#  If the item to remove does not exist, discard() will NOT raise an error.
# 3.pop()
# x = {"apple", "banana","xyz","grape"}
# x.pop()
# print(x)

# clear()
# x = {"apple", "banana", "cherry"}
# x.clear()
# print(x)
# # del()
# q=10
x = {"apple", "banana", "cherry"}
del x
print(x)

# Loop Items
# a = {"apple", "banana", "cherry"}
# for x in a:
#   print(x)




# operators
# 1. union()
set1 = {"apple", "banana", "cherry"}
set2 = {1, 2, 3,"apple"}
set3={5,2}
# set4 = set1.union(set2,set3)
# set4=set1|set2|set3
# print(set4)
#

# # # morethan two sets
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
# result = x.union(y,z)
# result=x|y|z
# print(result)

# and union operator
# set1 = {"apple", "banana", "cherry"}
# set2={1,2,3,4}
# set3=set1|set2
# print(set3)
# morethan two sets
# x = {"a", "b", "c"}
# y = {"f", "d", "a"}
# z = {"c", "d", "e"}
# result = x|y
# print(result)

# 2.intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# z=x&y
# print(z)
# morethan two sets
# x = {"a", "b", "c"}
y = {"c", "d", "e","b"}
z = {"f", "g", "c","b"}
# result = x.intersection(y, z)
# print(result)
# operator
# x = {"a", "b", "c"}
# y = {"c", "d", "e","b"}
# z = {"f", "g", "c","b"}
# result = x.intersection(y, z)
# print(result)

# morethan two sets
# x = {"a", "b", "c"}
# y = {"c", "d", "e","b"}
# z = {"f", "g", "c","b"}
# result = x&y&z
# print(result)

# another intersection operator intersection_update()

a = {'violet', 'indigo', 'blue', 'green', 'yellow'}
b = {'indigo', 'orange', 'red'}
# common_colors = a.intersection(b)
# print(common_colors)
# print(a)

# # intersection of two sets using intersection_update()
# a.intersection_update(b)
# print(a)






# difference()
#
x = {"google", "microsoft", "apple","banana"}
y = {"apple", "banana", "cherry"}
# z = x.difference(y)
# z=x-y
# print(z)










# operator
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# z={"asd","wer"}
# z = y-x
# print(z)

# difference_update()
# a = {'violet', 'indigo', 'blue', 'green', 'yellow'}
# b = {'indigo', 'orange', 'violet'}

# difference of two sets


# a.difference_update(b)
# a.difference_update(b)
# print(a)
# print(a)
# print(a)


# difference of two sets
# a.difference_update(b)
# print(a)








# symmetric_difference()
x = {"apple", "banana", "cherry","mango"}
y = {"google", "microsoft", "apple","mango"}
# z = y.symmetric_difference(x)
# print(z)


# # operator
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
#
# z = x^y
# print(z)


# symmetric_difference_update
a = {'violet', 'indigo', 'blue', 'red', 'yellow'}
b = {'indigo', 'orange', 'red'}

# # symmetric difference
# unique_items = a.symmetric_difference(b)
# print(unique_items)


# using symmetric_difference_update()
# a.symmetric_difference_update(b)
# print(a)




# methods


# 1.copy()
set1 = {5,6}
set2={1,2,3,4}
# set3 = set1.copy()
# print(set3)

# subset
# print(set1.issubset(set2))


# functions

# len
set1 = {1, 2, 3, 4, 5}
# set2 = len(set1)
# print(set2)

# set1 = {1, 2, 3, 4, 5}
# set2 = sum(set1,10)
# print(set2)
# or
# set1 = {1, 2, 3, 4, 5}
# print(sum(set1, 10))
# print(set2)



# min()
# set1 = {8, 2, 3, 4, 5}
# set2 = max(set1)
# print(set2)
# max()
# set1 = {1, 2, 3, 4, 5}
# set2 = max(set1)
# print(set2)


# frozen set
# fs = frozenset((1, 2, 3, 4))
# print(fs)

