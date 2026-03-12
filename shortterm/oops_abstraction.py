 # # abstract method

from abc import ABC, abstractmethod


class College(ABC):
    @abstractmethod
    def student1(self):
        pass


class Department(College):
    def student1(self):
        print("hello")

obj=College()
obj.student1()



# class Animal(ABC):
#     @abstractmethod
#     def move(self):
#         pass


#
# class Human(Animal):
#
#     def move1(self):
#         print("child class")
#
#
# class Snake(Animal):
#     def move(self):
#         print("hai")
#
# h = Human()
# h.move()
# h.move1()

# s = Snake()
# s.move()




