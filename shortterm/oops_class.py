# OOPs is a way of organizing code that uses objects and classes to represent real-world entities and their behavior.
# Benefits of OOP:
# Modularity: Code is easier to manage and debug.
# Reusability: Use existing code through inheritance.
# Scalability: Easy to expand for large applications.
# Security: Encapsulation hides sensitive data.


class Parent:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
        print("parent constructor")
    def method1(self):
        print("parent class")


class Child(Parent):
    def __init__(self,place,name,mark):
        self.place=place

        print("child constructor")
        super().__init__(name,mark)

    def method2(self):
        print(self.name,self.mark,self.place)

obj=Child("calicut","arun",85)
obj.method1()
obj.method2()






# class Student:
#     school = "Futura"   # Class variable
#
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark
#
#     def show(self):
#         print(self.name, self.mark, Student.school)
#
#     @classmethod
#     def change_school(cls, new_name):
#         cls.school = new_name   # Changing class variable
#
#
# s1 = Student("Arun", 80)
# s2 = Student("Meera", 90)
# s1.show()
# s2.show()
# # Change school using class method
# Student.change_school("Techno")
# print("After changing school:")
# s1.show()
# s2.show()


#
# class Student:
#     company="futura"
#
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#
#     def demotxt(self):
#         print(self.name,self.mark,Student.company)
#
#     @classmethod
#     def demo1(cls):
#         print(cls.company)
#     @staticmethod
#     def add(a,b):
#         print(a+b)
#
# obj=Student("abhi",95)
# Student.demo1()
# Student.add(10,20)
# print(obj.mark)


# class Employee:
#     # class variables
#     company_name = 'ABC Company'
#
#     def __init__(self, name, salary):
#         # instance variables
#         self.name = name
#         self.salary = salary
#
#     # instance method
#     def show(self):
#         print('Employee:', self.name, self.salary, self.company_name)
#
# emp1 = Employee("Harry", 12000)
# emp1.show()
# emp2 = Employee("Emma", 10000)
# emp2.show()


# instance method
# class Car:
#     def __init__(self,color,model,gps=False):
#         self.color=color
#         self.model=model
#         self.gps=gps
#     # get method/getter
#     def car_info(self):
#         print(f'model:{self.model}\n color:{self.color} \n gps:{self.gps}')
#
#     #     setter method/setter
#     def set_gps(self):
#         self.gps=True
#         print("gps enabled")
#
# car1=Car("red","2023")
# car1.car_info()
# car1.set_gps()
# car1.car_info()
# print(car1.gps)


# class method decorator

# class Car:
#     wheels=4
#     @classmethod
#     def get_count(cls):
#         print(cls.wheels)
#
#
# Car.get_count()


# static mthod
# class Car:
#     @staticmethod
#     def sum(a,b):
#         print(a+b)
# Car.sum(4,2)


# class variable
# class College:
#     def __init__(self):
#         print("parent constructor")
#     def method1(self):
#         print("parent class")
#
# class Student(College):
#     def __init__(self):
#         print("child constructor")
#         College.__init__(self)
#
#     def method2(self):
#         print("child class")
#
# obj=Student()
# obj.method1()
# obj.method2()


# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#         print(f"Account owner = {self.owner}, Balance = {self.balance}")
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited = {amount}. New balance = {self.balance}")
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew = {amount}. New balance = {self.balance}")
#         else:
#             print("Insufficient funds")
#
#     def get_balance(self):
#         print(f"Current balance = {self.balance}")
#
#
# account1 = BankAccount("Alice", 1000)
# account1.deposit(500)
# account1.withdraw(1200)
# account1.withdraw(500)
# account1.get_balance()


#deoratr

# def my_decorator(func):
#     def demo():
#         print("Before function execution")
#         func()
#         print("After function execution")
#     return demo
#
# @my_decorator
# def say_hello():
#     print("Hello!")
#
# say_hello()


# documentation
# help(classmethod)

# import builtins
# print(dir(builtins))
