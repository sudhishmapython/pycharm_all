

# common tasks
# 1.
# s: store sum of all numbers
# s = 0
# n = int(input("Enter number "))
# # run loop n times
# # stop: n+1 (because range never include stop number in result)
# for i in range(1, n + 1):
# #     # add current number to sum variable
#     s += i
# print("Sum is: ", s)

# 2.
# s: store sum of all numbers
# s = 0
# n = int(input("Enter number "))
# for i in range(1, n + 1, 1):
#     s += i
# print("\n")
# print("Sum is: ", s)

# 3.
# list1 = [10, 20, 30, 40, 50]
# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i],end=" ")

# 4.
# a = int(input("Enter value of a: "))
# b = int(input("Enter value of b: "))
# print(f"\na is {a} b is {b}")
# a = a + b
# b = a - b
# a = a - b
# print("\nafter swapping")
#
# print(f"a is {a} b is {b}")

# 5.
# val = input("Enter any character: ")
# if val in ['a','e','i','o','u']:
#     print(f"{val} is vowel")
# else:
#     print(f"{val} is consonent")

# a = 2
# b = 4
# if a >= b:
#     print("a is greater")
# else:
#     print("b is greater")




# 6.
# val1 = int(input("Enter value 1: "))
# val2 = int(input("Enter value 2: "))
# val3 = int(input("Enter value 3: "))
# print("\n before sorting",val1, val2, val3)
# s = []
# s.append(val1)
# s.append(val2)
# s.append(val3)
# s.sort()
# print("\n after sorting",s)


# 7
# string_ = "adam is a boy and adam loves to play cricket."
# x = input("Enter the word you want to check: ")
# main = string_.split(" ")
# count = 0
# for i in range(len(main)):
#     if main[i] == x:
#         count += 1
# print(count)

# 8. factorial of a number
# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print("Factorial of", num, "is", factorial)


# 11

# str1="hello world"
# sum=0
# for i in str1:
#     vowels="aeious"
#     if i in vowels:
#         sum+=1
#         print(i)
# print(sum)

#12

# str1="hello calicut"
# str2=""
# for i in str1:
#     if i not in str2:
#         str2+=i
# print(str2)



# prayag

# Prompt the user to enter a three-digit number
# num = int(input("Enter a three-digit number: "))
#
# # Initialize sum to 0
# total_sum = 0
#
#
#     # Use a while loop to sum the digits
#     while num > 0:
#         digit = num % 10  # Get the last digit
#         total_sum += digit  # Add the digit to the total sum
#         num //= 10  # Remove the last digit
#
#     # Print the result
#     print("The sum of the digits is:", total_sum)
# else:
#     print("Invalid input! Please enter a three-digit number.")

# or

# number = input("Enter a  number: ")
# total = 0
# index = 0
# while index < len(number):
#     total += int(number[index])
#     index += 1
# print(total)


# 1
# str1 = "PYnative"
# print("Original String is:", str1)
# str1 = str1[::-1]
# print("Reversed String is:", str1)

# 2
# num1 = int(input("Enter first number "))
# num2 = int(input("Enter second number "))
# res = num1 * num2
# print("Multiplication is", res)

# 3.
# txt = " Hello World "
# print(txt)
# print(txt.strip())




# list
# 1.
# fruits = ["apple", "banana", "cherry"]
# fruits[0]="kiwi"
# print(fruits)
# 2.
# fruits = ["apple", "banana", "cherry"]
# print(len(fruits))
# 3
# fruits = ["apple", "banana", "cherry","mango","papaya","watermelon","grape"]
# print(fruits[3:6])

# 4
# my_list = []
# if my_list == []:
#     print("The list is empty")
# else:
#     print("not")

# 5
# numbers = [1, 2, 3, 4, 5, 6, 7]
# res = []
# for i in numbers:
#     res.append(i * i)
# print(res)

#tuple
# 1.
# tuple1 = (50, 10, 60, 70, 50)
# print(tuple1.count(50))
# 2.
# x = ("apple", "banana", "cherry", "grape")
# y = list(x)
# y[2] = "kiwi"
# x = tuple(y)
# print(x)

# 3.
# tuple1 = (11, 22)
# tuple2 = (99, 88)
# tuple1, tuple2 = tuple2, tuple1
# print(tuple2)
# print(tuple1)

# 4.
# tuple1 = (11, 22, 33, 44, 55, 66)
# tuple2 = tuple1[3:-1]
# print(tuple2)




# sets
# 1.
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")

# 2.
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
#
# print(set1.intersection(set2))

# 3.
# Create two sets
# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 3}
# abc = set2.issubset(set1)
# print("Set 2 is a Subset of Set 1:", abc)


# 4.

# input_list = [1, 2, 2, 3, 4, 4, 5]
# unique_elements = list(set(input_list))
# print("Original List:", input_list)
# print("List with Duplicates Removed:", unique_elements)


# dictinry
# 1.
# car =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# car["color"]="red"

# 1.1.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# print(car.get("model"))

# 2
mark = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
# print(min(mark, key=mark.get))





# 3
sample = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

sample['emp3']['salary'] = 8500
# print(sample)









# while loop
#1. program to display numbers from 1 to 5
# i = 1
# n = 5
# while i <= n:
#     print(i)
#     i = i + 1

# (reverse)
# count = 5
# while count > 0:
#     print(count)
#     count -= 1

# 2.usetinput

# password = input("Enter a password: ")
# while len(password) < 8:
#     print("Password must be at least 8 characters long.")
#     password = input("Enter a password: ")
# print("Password is valid!")


# function


#     def sum():
#     num1 = 5
#     num2 = 3
#     total = num1 + num2
#     print("Sum:", total)
# sum()

# 2.(function with argument)
# def area(length, width):
#     area = length * width
#     print("Area of rectangle:", area)
# area(5, 3)

# 3.
# def square(y):
#     return y*y
# for i in range(1,11):
#     print(square(i))

# 4.
# def first_last_same(numberList):
#     print("Given list:", numberList)
#
#     first_num = numberList[0]
#     last_num = numberList[-1]
#
#     if first_num == last_num:
#         return True
#     else:
#         return False
#
#
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))
#
# numbers_y = [75, 65, 35, 75, 30]
# print("result is", first_last_same(numbers_y))






# for loop
# list1=[1,2,3,4,5]
# sum=0
# for i in list1:
#     sum=sum+i
#     print(sum)

# or

# for i in list1:
#     print(i+2)


# break
# while True:
#     name = input("Enter your name (or 'quit' to exit): ")
#     if name == 'quit':
#         break
#     print(f"Hello, {name}!")

# continue
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for num in numbers:
#     if num % 2 == 0:
#         continue
#     print(num)


# mutiplication table
# def multiplication():
#     num=int(input("Enter a number:"))
#     limit=int(input("Enter the limit:"))
#     for i in range(1,limit+1):
#         print(i,"X",num,"=",i*num)
# multiplication()


# def add(a, b):
#     result = a + b
#     return result
#
# add(2, 2)



# Reading a file line by line:
# file = open("example.txt", "r")
# for line in file:
#     print(line)
# file.close()


# recursion task
# def summation(n):
#     if n == 1:
#         return 1
#
#     else:
#         return n+summation(n-1)
#
# print(summation(5))


# 2

# def list_sum(num_List):
#     if len(num_List) == 1:
#         return num_List[0]
#     else:
#         return num_List[0] + list_sum(num_List[1:])
# print(list_sum([2]))



# lambda
# 1
# r = lambda a : a + 15
# print(r(10))
# r = lambda x, y : x * y
# print(r(12, 4))



# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda x: x % 2 == 0, nums))
# print(even)



# 2
# Given list of integers
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print("Original list of integers:")
# print(nums)
#
# even_nums = [x for x in nums if (lambda x: x % 2 == 0)(x)]
# print("Even numbers from the said list:")
# print(even_nums)
#
# odd_nums = [x for x in nums if (lambda x: x % 2 != 0)(x)]
# print("Odd numbers from the said list:")
# print(odd_nums)

#




# List comprhsn
# 1
lst1=[2, 4, 6, 8, 10, 12, 14]
# lst2 = [i**2 for i in lst1]
# print(lst2)
# 2
# lst2 = [i**2 for i in lst1 if i**2>50]
# print(lst2)

# set

# sentence = "welcome to kerala nice to meet you."
# word_lengths = {len(word) for word in sentence.split()}
# print(sentence)
# print(word_lengths)

# dictionary
# Generating odd number with their cube values with using dictionary comprehension
# dictdemo = [1, 2, 3, 4, 5, 6, 7]
# dict5 = {var: var ** 3 for var in dictdemo if var % 2 != 0}
# print(dict5)


# file and exception
# 1
# def open_file(filename):
#     try:
#         file = open(filename, 'r')
#         contents = file.read()
#         print("File contents:")
#         print(contents)
#         file.close()
#     except FileNotFoundError:
#         print("Error: File not found.")
# # Usage
# file_name = input("Input a file name: ")
# open_file(file_name)

# 2
# def test_index(data, index):
#     try:
#         result = data[index]
#         # Perform desired operation using the result
#         print("Result:", result)
#     except IndexError:
#         print("Error: Index out of range.")
#
#
# nums = [1, 2, 3, 4, 5, 6, 7]
# index = int(input("Input the index: "))
# test_index(nums, index)




# 3
# try:
#     n = int(input("Input a number: "))
#     print(n)
# except KeyboardInterrupt:
#     print("keyboard interruption")






# 4
# Count of words in text file

# def read_data():
#     f = open("xyz.txt",'r')
#     s = f.read()
#     d=s.split()
#     count = 0
#     for i in d:
#         print(i)
#         count = count+1
#     print("Total words are",count)
#
# read_data()

# output
# Total words are 20



# class
# 1
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# modelX = Vehicle(240, 18)
# print(modelX.max_speed, modelX.mileage)

# 2
# class Vehicle:
#     pass

# 3
# class Vehicle:
#     # Class attribute
#     color = "White"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 180, 12)
# print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
#
# car = Car("Audi Q5", 240, 18)
# print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)



# 4
# previous_num = 0
#
# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     previous_num = i




# inheritence
# class Vehicle:
#     # Class attribute
#     color = "White"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# School_bus = Bus("School Volvo", 180, 12)
# # print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)
#
# car = Car("Audi Q5", 240, 18)
# print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)


# Extra

# def sum(x, y):
#     sum = x + y
#     if sum in range(15, 20):
#         return 20
#     else:
#         return sum
#
# print(sum(2,4))
# print(sum(10,6))


# sum = 0
#
# while True:
#     num = int(input("Enter a number"))
#     if num < 0:
#         break
#     sum += num
#
# print(f"The sum of all positive numbers: {sum}")


# fibinnaci

# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         print(b, end=' ')
#         temp = b
#         b = a + b
#         a = temp
#
# fibonacci(10)


#. Replace the word "old" with "new" in a file.
# file=open('xyz.txt', 'r')
# content = file.read()
# content = content.replace('old', 'new')
#
# file=open('xyz.txt', 'w')
# file.write(content)
