
# process objects differently depending on the class type or data type. 










# class College:
#     def add(self,name):
#         print(name)
#
#
# class Student(College):
#     def add(self,name):
#         College.add(self,name)
#         print("child method")
#
#
#
# obj=Student()
# obj.add("abc")



#
# class parrot:
#     def fly(self):
#         print('parrot can fly')
#     def swim(self):
#         print('parrot cant swim')
# class penguin:
#     def fly(self):
#         print('penguin cant fly')
#     def swim(self):
#         print('penguin can swim')
# def test(bird):
#     bird.fly()
#     bird.swim()
#
# obj=parrot()
# test(obj)
# obj1=penguin()
# test(obj1)



# __truediv__,__mul___,__floordiv__, __mod__

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
#     def __add__(self, other):
#         return self.price + other.price
#
#
# bread = Product("Bread", 40)
# milk = Product("Milk", 30)
#
# print(bread + milk)





# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         return f"Name: {self.name}, Marks: {self.marks}"
#
#
# s1 = Student("Rahul", 85)
# print(s1)























# a=10
# b=2
# c=a+b
# print(c)

# method overloading(compile time)

# class A:
#     def product(self,a,b,c=0,d=0):
#         p = a * b*c
#         print(p)
#
#     # def product(sef,a,b):
#     #     p = a * b
#     #     print(p)
#
# ob=A()
# ob.product(1,2,3)

# to use

# class A:
#     def product(self,a,b,c=0,d=0):
#         p = a +b+c+d
#         print(p)
#
# ob=A()
# ob.product(1,2,3)

# method overriding(run time)
# #
# class Vehicle:
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#     def show(self):
#         print('Details:', self.name, self.color, self.price)
#     def max_speed(self):
#         print('Vehicle max speed is 150')
#     def change_gear(self):
#         print('Vehicle change 6 gear')
# class Car(Vehicle):
#     def max_speed(self):
#         print('Car max speed is 240')
#         super().max_speed()
#         # Vehicle.max_speed(self)
#     def change_gear(self):
#         print('Car change 7 gear')
#         # super().change_gear()
#
# car = Car('Car x1','Red', 20000)
# car.show()
# car.max_speed()
# car.change_gear()




# overloading

# class person:
#     def message(self,name=None):
#         if name==None:
#             print('hello')
#         else:
#             print('hello' +name)
# obj=person()
# obj.message('futura')


# class CartItem:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __add__(self, other):
#         return (self.price * self.quantity) + (other.price * other.quantity)
#
#     def __mul__(self, value):
#         return self.price * self.quantity * value
#
#     def __str__(self):
#         return f"{self.name} Total = {self.price * self.quantity}"
#
#
# item1 = CartItem("Pen", 10, 5)
# item2 = CartItem("Book", 50, 2)
#
# print(item1 + item2)   # total price
# print(item1 * 2)       # double quantity value