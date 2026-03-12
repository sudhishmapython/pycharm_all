# class College:
#     def __init__(self):
#         print("parent constructor")
#     def method1(self):
#         print("first method")
#     def method2(self):
#         print("second method")
# class Student(College):
#
#     def __init__(self):
#         super().__init__()
#         print("child constructor")
#     def chilmethod1(self):
#         College.method2(self)
#         print("child method")
#
# obj=Student()
# obj.method1()
# obj.chilmethod1()








# class College:
#     college_name = "ABC College"
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
#
#     def demo.txt(self):
#         print("first data",self.name)
#     def demo1(self):
#         print("second data",self.mark)
#
#     @classmethod
#     def get_college_name(cls):
#         print(f"College Name (Class Variable): {cls.college_name}")
#
# class Student(College):
#     def __init__(self,course,name,mark):
#         self.course=course
#         College.__init__(self,name,mark)
#
#     def demo2(self):
#         print(self.name,self.mark,self.course)
#
# obj=Student("python","abc",95)
# obj.demo.txt()
# obj.demo2()
#
# print(Student.college_name)




# class Student:
#     def __init__(self, name, mark):
#         self.name = name
#         self.mark = mark
#     def method1(self):
#         print(self.name)
# class College(Student):
#     def __init__(self,age,name,mark):
#         self.age = age
#         Student.__init__(self,name,mark)
#
#     def method2(self):
#         print(self.age)
#
# obj=College(23,"abc",98)
# obj.method1()
# obj.method2()


    # def info(self):
    #     print(self.name, self.mark)





# class Vehicle:
#
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#
#     def info(self):
#         print(self.name, self.color, self.price)
#
# class Car(Vehicle):
#
#     def change_gear(self, no):
#         print(self.name, 'change gear to number', no)
#
#
# car = Car('BMW X1', 'Black', 35000)
# car.info()
# car.change_gear(5)



# types of inheritance

# 1. single inheritance

# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
# class Child(Parent):
#     def func2(self):
#         print("This function is in child class.")
#
# object = Child()
# object.func1()
# object.func2()


# 2. multilevel

# class Grandfather:
#     def func1(self):
#         print("This function is in grandparent class.")
# class Father(Grandfather):
#     def func2(self):
#         print("This function is in parant class.")
#
# class Child(Father):
#     pass
#
# c=Child()
# c.func1()

# 2.
# class Grandfather:
#
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername
#
# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#
#         # invoking constructor of Grandfather class
#         Grandfather.__init__(self, grandfathername)
#
# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#
#         Father.__init__(self, fathername, grandfathername)
#
#     def print_name(self):
#         print('Grandfather name :', self.grandfathername)
#         print("Father name :", self.fathername)
#         print("Son name :", self.sonname)
#
#
# s1 = Son('Prince', 'Rampal', 'Lal mani')
# print(s1.grandfathername)
# s1.print_name()


# class Vehicle():
#     def __init__(self, name, model, price):
#         self.name = name
#         self.model = model
#         self.price = price
#
#     def details(self):
#         print(self.name, self.model, self.price)
# class Car(Vehicle):
#     def __init__(self,name,model,price,no):
#         self.no=no
#         super().__init__(name,model,price)
#
#     def demo.txt(self):
#         print(self.name,self.model,self.no)
# class Shop(Car):
#     def __init__(self,name,model,price,no,shopname):
#         self.shopname=shopname
#         Car.__init__(self,name,model,price,no)
#
#     def demo1(self):
#         print(self.name,self.model,self.price,self.no,self.shopname)
#
#
#
# car = Shop("bmw",2023,25000,6,"abc")
# car.demo1()














# 3. multiple inheritance

# class Mother:
#
#     def mother(self):
#         print("its method1")
#
# class Father:
#     def father(self):
#         print("its method2")
# class Son(Mother, Father):
#     pass
#
# s1 = Son()
# s1.mother()
# s1.father()


# 4. Hierarchical Inheritance:

# class Parent:
#     def func1(self):
#         print("This function is in parent class.")
#
#
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")
#
#
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")
#
#
# object1 = Child1()
# object2 = Child2()
# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()


#  5.Hybrid Inheritance:

# class School:
#     def func1(self):
#         print("This function is in school.")
#
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1. ")
#
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.")
#
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")
#
#
# object = Student3()
# object.func1()
# object.func2()



# init method

# class A:
#     def __init__(self):
#         print("first data")
#
# class B(A):
#
#     def __init__(self):
#         print("second data")
#
# b=B()


# super keyword


# class A:
#     def __init__(self):
#         print("first data")
#
# class B(A):
#
#     def __init__(self):
#         print("second data")
#         super().__init__()
# b=B()



# 2

# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
#
#     def area(self):
#         return self.length*self.breadth

# rect=Rectangle(6,3)
# print(rect.area())

# class Square(Rectangle):
#     def __init__(self,side):
#         self.side=side
#         Rectangle.__init__(self,side,side)


# sqr=Square(5)
# print(sqr.area())