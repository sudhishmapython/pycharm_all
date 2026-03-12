


# A decorator is a function that takes another function as input, modifies its behavior, and returns a new function.
# function can be treated as variables (first class variables)
#


# def function1():
#     print("calicut")
# function1()
#
# # # first class variable
# a=function1
# a()






#
# def square(n):
#     return 2*n
#
# def add(a,b):
#     return a+b
#
# print(square(add(5,5)))


# decorator

# def decorate(func):
#     def add(a,b):
#         result=func(a+b)
#         return result
#     return add
# # #
# @decorate
# def square(x):
#     return 2*x
#
# print(square(5,1))





# Define a decorator function
# def my_decorator(fun):
#     def demo():
#         print("Something is happening before the function is called.")
#         fun()
#         print("Something is happening after the function is called.")
#
#     return demo
# #
# @my_decorator
# def function1():
#     print("Hello!")
# #
# function1()


# a = my_decorator(function1)
# a()

