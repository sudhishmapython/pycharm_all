



# declaration
# tuple1=("apple","banana","cherry",1,2)
# tuple2=("abc", 34, True, 40, "male")
# print(tuple1[0])
# print(tuple2)
# print(type(tuple1))
# tuple2=("apple",)

# tuple() contructor
# a = tuple(("apple", "banana", "cherry"))
# print(a)



# access tuple items
# tuple1 = ("apple", "banana", "cherry")
# tuple1[3]="abc"
# print(tuple1)

# negative indexing
# tuple1 = ("apple", "banana", "cherry")
# print(tuple1[-1])

# range of index
# tuple1 = ("apple", "banana", "cherry","pappaya","grape")
# print(tuple1[2:4])


# Check if "apple" is present in the tuple:
# tuple1 = ("apple", "banana", "cherry")
# if "apple" in tuple1:
#   print("Yes, 'apple' is in the fruits tuple")

# Loop Through a Tuple
# x = ("apple", "banana", "cherry")
# for y in x:
#   print(y)


# Change Tuple Values
# x = ("apple", "banana", "cherry")
#
#
# y=list(x)
# print(y)
# y[0]="abc"
# x=tuple(y)
# print(x)


# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)




# Add Items
# 1.Convert into a list
# x = ("apple", "banana", "cherry")
# y = list(x)
# y.append("orange")
# y.insert(1,"grape")
# x = tuple(y)
# print(x)

# 2.Add tuple to a tuple.
x = ("apple", "banana", "cherry")
y = ("orange",)
x += y
# print(x)

# Remove Items
# 1.remove()
# x=("apple", "banana", "cherry","pappaya","grape")
# y=list(x)
# y.remove("cherry")
# x=tuple(y)
# print(x)

# 2. delete the tuple completely:
# del x
# print(x)


# Concatenating two Tuples
# tuple1 = (1, 2, 3, 4, 5)
# tuple2 = (3, 4, 5, 6, 7)
# tuple3=tuple1+tuple2
# print(tuple3)

# Multiply Tuples
# tuple1 = ("apple", "banana", "cherry")
# mytuple = tuple1 * 2
# print(mytuple)

# methods
# 1.count()
# x=("apple", "banana", "cherry","apple","pappaya","grape")
# print(x.count("apple"))

# 2.index()
# x=("apple", "banana", "cherry","apple","pappaya","grape")
# print(x.index("grape"))

# functions
x=("banana","apple", "cherry")
numbers = (10, 20, 30, 20, 40)
# m,y,z=x
# print(m,y,z)
# 1.len()
# print(len(x))
#  2.max()
# print(min(x))
# 3. min()
# print(min(x))
# 4. sum
# print(sum(numbers))

