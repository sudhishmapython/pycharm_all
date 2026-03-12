



# list declaration
# list1 = ["apple", "banana", "cherry","cherry",2,4,True,"apple"]
#
# print(list1)
# print(len(list1))


# Indexing
list1=["a","b",3,2,4]
# print(list1[2])

# negative indexing
my_list = [10, 20,'Jessa',12.50,'Emma']
# print(my_list[-1])


# length
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# all datatype
# list1 = ["abc", 34, True, 40, "male"]
# print(list1)

# list constructor

# a = list(("apple", "banana", "cherry"))
# print(a)


# list slicing
my_list1 = [10, 20, 'Jessa', 12.50, 'Emma', 25, 50]
# print(my_list1[:5])



# my_list = [5, 8, 'Tom', 7.50, 'Emma']

# slice first four items
# print(my_list1[:5])


# print every second element  with a skip count 2
# print(my_list1[::3])


# reversing the list
# print(my_list[::-1])

# Without end_value
# print(my_list1[5:])

# negative slice
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])




# Check if Item Exists
# demolist = ["apple", "banana", "cherry"]
# if "apple" in demolist:
#     print("Yes, 'apple' is in the fruits list")
# else:
#     print("not in  fruits list")


# iteration
# my_list = [5, 8, 'Tom', 7.50, 'Emma']
# for item in my_list:
#     print(item,end=" ")





# Change Item Value
# a = ["apple", "banana", "cherry","orange","mango"]
# a[1:3]=[10,50,"cherry"]
# print(a)
# a[1:3] = ["blackcurrant","grape"]
# print(a)



#Change a Range of Item Values
# a = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#
# a[1:3]=[85]
# print(a)



# a[1:3] = ["blackcurrant", "watermelon"]
# print(a)
#or
# b = ["apple", "banana", "cherry"]
# b[1:2] = ["blackcurrant", "watermelon"]
# print(b)
# or
# c = ["apple", "banana", "cherry"]
# c[1:2] = ["watermelon","apple"]
# print(c)

# add

# insert item to string
# a = ["apple", "banana", "cherry"]
# a.insert(2,"watermelon")
# print(a)


# Append Items
# b = ["cherry"]
# b.append("orange")
# print(b)

# extend
# a = ["apple", "banana", "cherry"]
# b=[1,2]
# a.extend(b)
# print(a)






# Modify the items of a List
# my_list = [2, 4, 6, 8, 10, 12]

# modify single item
# my_list[0] = 20
# print(my_list)

# modify from 1st index to 4th
# my_list[1:4] = [40, 60, 80]
# print(my_list)

# modify from 3rd index to end
# my_list[3:] = [80, 100, 120]
# print(my_list)


# all items modify
# list1 = [10, 20, 30, 40, 50, 60]
# list2=[]
# print("Original list ")
# print(list1)
# print("After incrementing each element of list by 2")
# for i in range(len(list1)):
#     # list1[i] = list1[i] + 2
#     list2.append(list1[i]+2)
# print(list2)





# remove items from list
# 1.remove()

# str = ["apple", "banana", "cherry","grape","banana"]
# str.remove("banana")
# print(str)


# 2.pop()
# abc = ["apple", "banana", "cherry"]
# abc.pop(1)
# print(abc)



#  or
# abc.pop(1)
# print(abc)


# 3.del()
# abc = ["apple", "banana", "cherry",4,6,9]
# del abc[1]
# print(abc)


# 4.clear()
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)




# 5.count()
# fruits = ['apple', 'grape', 'apple', 'grape']
# print(fruits.count('grape'))
# print(len(fruits))

# # 6.sort()
# fruits = [1,2,8,5,3]
# fruits.sort()
# print(fruits)

# 7.reverse()
# fruits = ['cherry','apple', 'banana', 'cherry', 'banana']
# fruits.reverse()
# print(fruits)


#



# functions
# 1. len()
# fruits = [1,5,7,5]
# print(len(fruits))
# 2. min()
# fruits = [1,3]
# print(max(fruits))


 
# 3. max()
# fruits = ['apple', 'banana', 'cherry', 'mango']
# print(max(fruits))






# join of two lists
# str = [1, 2, 3]
# str1 = [4, 5, 6]
#
# str2 = str + str1
# print(str2)
# Using extend() method
# str.extend(str1)
# print(str)


# list1=[10,20,30,40,50]
# list2=[]
# for i in range(len(list1)):
#     # print(list1[i])
#     list2.append(list1[i]+10)
#
# print(list2)



fruits = [1,2,3,4,5]
total=0
for i in fruits:
    total+=i
print(total)