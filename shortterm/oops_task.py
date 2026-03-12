# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def show(self):
#         print("Name:", self.name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)
#
#     def total_value(self):
#         return self.price * self.quantity
#
#
# class Electronic(Product):
#     def __init__(self, name, price, quantity, brand, warranty):
#         super().__init__(name, price, quantity)
#         self.brand = brand
#         self.warranty = warranty
#
#     def show(self):
#         super().show()
#         print("Brand:", self.brand)
#         print("Warranty:", self.warranty, "years")
#         print("Total Value:", self.total_value())
#         print()
#
#
# class Clothing(Product):
#     def __init__(self, name, price, quantity, size, material):
#         super().__init__(name, price, quantity)
#         self.size = size
#         self.material = material
#
#     def show(self):
#         super().show()
#         print("Size:", self.size)
#         print("Material:", self.material)
#         print("Total Value:", self.total_value())
#         print()
#
#
# l1 = Electronic("Laptop", 60000, 10, "HP", 2)
# c1 = Clothing("T-Shirt", 500, 50, "L", "Cotton")
#
# l1.show()
# c1.show()


# 2


class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name, " Company:", Employee.company)

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @staticmethod
    def add(a,b):
        print(a+b)

e1 = Employee("John")
e1.show()
e1.add(10,20)

Employee.change_company("Microsoft")
e1.show()
