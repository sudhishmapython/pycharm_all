# This ensures the internal state of the object is protected and can only be
# modified in a controlled way.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.__salary=salary
    def disply(self):
        print("disply data")
    def getdata(self):
        return self.__salary
    def set_data(self):
        self.__salary=1000


obj=Employee("abc",85)
obj.disply()
print(obj.getdata())
obj.set_data()
print(obj.getdata())

# class Student:
#     def __init__(self):
#         self.a="data1"
#         self.__b=10
#
#     def method1(self):
#         print("demo")
#
#     def getmethod(self):
#         return self.__b
#
#     def set_data(self):
#         self.__b="private data "
#
#
# obj=Student()
# print(obj.getmethod())
# # print(obj.getmethod())
# obj.set_data()
# print(obj.getmethod())

# obj.set_data()
# print(obj.method1())
#


# class Base:
#     def __init__(self):
#         self.a = "first data"
#         self.__c = "second data"
#
#     def method1(self):
#         return self.__c
#
#
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         print("Calling private member of base class: ")
#         print(self.method1())
#
#
#
# obj1 = Derived()
# print(obj1.method1())








# class B# Using getter method

# class Base:
#     def __init__(self):
#         self.a=80
#         self.__c = 10
#     def get_c(self):
#         return self.__c
#     #
#     def set_c(self, value):
#         self.__c = value
#
# class Derived(Base):
#     def __init__(self):
#         Base.__init__(self)
#         print("Calling private member of base class:")
#         print(self.get_c())  # Using getter method


# obj1 = Derived()
# print(obj1.a)
# print(obj1.get_c())
# obj1.set_c(20)  # Using setter method
# print(obj1.get_c())


# Direct access to __c is restricted
# # obj1.__c = 10  # This line will cause an AttributeError



# protected
# class Parent:
#     def __init__(self):
#         self._value = 10   # protected variable
#
# class Child(Parent):
#     def show_value(self):
#         print("Accessing protected variable from child:", self._value)
#
#
# c = Child()
# c.show_value()
# c._value=-700
# print("Direct access:", c._value)



# task -authenticatn

# class User:
#     def __init__(self, username):
#         self.username = username
#         self.__password = None   # Private variable
#
#     # Setter method
#     def set_password(self, new_password):
#         if len(new_password) < 6:
#             print("Password must be at least 6 characters")
#         else:
#             self.__password = new_password
#             print("Password set successfully")
#
#     # Check password
#     def check_password(self, input_password):
#         if self.__password is None:
#             print("Password not set")
#         elif input_password == self.__password:
#             print("Login Successful")
#         else:
#             print("Invalid Password")
#
#
# u1 = User("rahul")

# u1.set_password("123")        # Invalid
# u1.set_password("123456")     # Valid
#
# u1.check_password("123456")   # Correct password
# u1.check_password("000000")   # Wrong password


