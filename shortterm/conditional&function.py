
# 1. if
# num1 = 10
# num2 = 20
# num3 = 15
#
# # Comparisons to find the largest number
# if num1 >= num2 and num1 >= num3:
#     largest = num1
# elif num2 >= num1 and num2 >= num3:
#     largest = num2
# else:
#     largest = num3
#
# print("The largest number is:", largest)


# a = 2
# b = 2
# if b > a:
#     print("b is greater than a")


# 2. if-else
# if b > a:
#    print("b is greater than a")
# else:
#     print("a is greater than b")

# 3. if-elif
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")

# 4. if-elif-else
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")

# 5. nested if-else
# num = 15
# if num >= 0:
#     if num == 0:
#         print("Zero")
#     else:
#         print("Positive number")
# else:
#     print("Negative number")

# while loop    -->while loop we can execute a set of statements as long as a condition is true.

# count = 1
# while count <= 5:
#     print(count)
#     count+=1
#


# for loop -->A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


# n = 4
# for i in range(0, n):
#     print(i)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

#   and
# for x in "banana":
#   print(x)

# and (numbers using range)
# for x in range(1,11,2):
#     print(x)

n = 10
sum_natural = 0
# for i in range(1, n + 1):
#     sum_natural += i
# print("Sum of first", n, "natural numbers is:", sum_natural)


# i=1
# while i<=n:
#     sum_natural +=i;
#     i +=1
# print(sum_natural)


# break
# break statement in a for loop
# fruits = ["apple", "grape","banana", "cherry","mango"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

# break statement in a while loop
# count = 0
# while count < 5:
#     if count == 3:
#         break
#     print(count)
#     count += 1
#


# continue
# continue statement in a for loop
# fruits = ["apple", "banana", "cherry","grape"]
# for fruit in fruits:
#     if fruit == "banana":
#         continue
#     print(fruit)

# continue statement in a while loop
# count = 0
# while count < 5:
#     count += 1
#     if count == 3:
#         continue
#     print(count)


# pass
# pass statement in an if-else statement
# x = 80
# if x > 10:
#     print("x is greater than 10")
# else:
#     pass



a=10
b=20





# def demo.txt(a,b):
#     c=a+b
#     return c
#
#
# d=demo.txt(20,40)
# print(d)
#
# demo.txt(200,404)
#















# function
# 1.
# def my_function():
#   print("Hello from a function")
# my_function()

# 2.
# def display_message():
#     message = "This is a predefined message."
#     print(message)
# display_message()


# function with argument
# 1.
# def my_function(fname,name):
#   print("my name is",fname,name)
# my_function("appu","anagha")


# 2. Function to concatenate two strings:
# def concate(string1, string2):
#   result = string1 + string2
#   print("Concatenated string:", result)
# concate("Hello", " world!")



x=40
y=70








# types of arguments
# 1. positional arguments:- based on position


# def fun(b,c,a):
#     print(f"hai {a},{b},{c}")
# fun(1,2,3)
#



# 2.keyword argument:-dont want to send by position

# def person(name,age,salary):
#     print(name,age,salary)
# person(age=52,name="abhi",salary=25000)
#
#



# 3. default arguments:- by giving default value,right to left set values and give some value that take taht value not default value


# def fun(a,b,c=0,d=0):
#     print(a,b,c,d)
# fun(1,2,3)

# 4. arbitary positional arguments:-using * ,we can any number of arguments and it is stores as tuple.

# def fun(a,b,*args):
#     print(a,b,args)
# fun(1,6,8,5,9,2,5,8,6)

# # and
# def fun(a,b,*args):
#     print(a,b,args)
#     print(args)
# fun(1,2,3,4,5,"a",5,8)

# To find sum
# def fun(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# #
# fun(1,2,2,2)

# and


# 5.arbitary keyword arguments:-using ** and it is stored as dictionary (key value pair).

# def person(name,**args):
#     print(name,args)
# person(name="abc",age=45,location="clt",salary=25000)

# and

# def person(**details):
#     for key,val in details.items():
#         print(key,val)
# person(name="abc",age=45,location="clt",salary=25000)


# lambda function(anonymous function)

def recursive_fun(n):
    if n<=1:
        return 1
    else:
        return n*recursive_fun(n-1)

print(recursive_fun(5))





# x,y=11,20
# data=lambda x:print("even") if x%2==0 else print("odd")
# data(x)




# demo1=lambda x,y,z:x+y+z
# print(demo1(1,2,3))


# Immediately called without variable
# print((lambda x: x*2)(4))  # 8
#

# list1 = [1, 2, 3, 4, 5, 6, 7]

# list2=list(map(lambda  x: x+2,list1))
# list2=list(filter(lambda x:x%2==0,list1))
# print(list2)
#
#
# list2=list(map(lambda x:x+2,list1))
# print(list2)



# list2=list(filter(lambda x:x%2==0,list1))
# print(list2)



# list2=list(map(lambda x:x*x,list1))



# list4 =lambda x: print("even") if x % 2 == 0 else print("Odd")
# list4(2)
# list4(2)



# even=list(filter(lambda x:x%2==0, numbers))
#
# print(even)


#
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)


# nums = [1, 2, 3, 4]
# doubled = list(map(lambda x: x * 2, nums))
# print(doubled)  # Output: [2, 4, 6, 8]







#
# lamp=lambda a,b:print(a+b)
# lamp(10,20)


# words = ['madam', 'apple', 'level', 'world']
# palindromes = list(filter(lambda x: x == x[::-1], words))
# print(palindromes)  # ['madam', 'level']
#



# sum1=lambda a,b,c:print(a+b+c)
# sum1(1,3,2)


# sum=lambda x,y,z:print(x+y+z)
# sum(2,2,4)
# or
# sum=lambda x,y:print(x+y)
# sum(2,4)

# def my_fun(x):
#     return lambda a:a*x
# y=my_fun(10)
# print(y(2))


# return value
# 1.
# def sum(num1,num2):
#     return num1+num2
# result=sum(2,2)
# print(result)
# 


# 2.
# def calculate_sum(num1, num2):
#     total = num1 + num2
#     return total
# print("Sum:",calculate_sum(5, 3))
# or
# result=calculate_sum(5, 3)
# print(result)
# d=result+70
# print(d)


# recursive




# def my_func(n):
#     return lambda x: x * n
#
# doubler = my_func(2)
# print(doubler(5))
#

 # 9.sorted
# fruits = [3, 1, 4, 2]
# new_fruits = sorted(fruits)
# print(fruits)
# print(new_fruits)



# 8. reversed
# fruits = ['apple', 'banana', 'cherry']
# rev = reversed(fruits)
# print(list(rev))
# or
# n = "abc"
# rev = reversed(n)
# print(''.join(rev))


# my_list = [1, 2, 3, 4, 5, 6]
# odd_numbers = list(filter(lambda x: x % 2 != 0, my_list))
# print(odd_numbers)


# factorial(3)          # 1st call with 3
# 3 * factorial(2)      # 2nd call with 2
# 3 * 2 * factorial(1)  # 3rd call with 1
# 3 * 2 * 1             # return from 3rd call as number=1
# 3 * 2                 # return from 2nd call
# 6                     # return from 1st call



# def recursive_fact(n):
#     if n <= 1:
#         return n
#     else:
#         return n * recursive_fact(n - 1)
#
# print(recursive_fact(5))



# def digit_count(n):
#     if n==0:
#         return 0
#     else:
#         return 1+digit_count(n//10)
#
#
#
# print(digit_count(12345))






# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)
#
# # Example: print the 10th Fibonacci number
# print(fibonacci(10))  # Output: 55
