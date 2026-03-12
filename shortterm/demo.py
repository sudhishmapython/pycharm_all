# *
# * *
# * * *
# * * * *

# for i in range(1,5):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5,0,-1):
#     for j in range(i):
#         print("*", end="  ")
#     print()









list1=[1,2,3,4,5]











# class College:
#     def __init__(self):
#         print("parent constructor")
#     def method1(self):
#         print("parent class")
#
#
# class Student(College):
#     def __init__(self):
#         print("child constructor")
#         College.__init__(self)
#     def method2(self):
#         print("child class")
#
#
# obj=Student()
#
# obj.method1()
# obj.method2()
#
#
#
#
#
#
# # class TaskManager:
# #     def __init__(self):
# #         self.tasks = []
# #
# #     def add_task(self, task):
# #         self.tasks.append(task)
# #         print(f"Task added: '{task}'")
# #
# #     def remove_task(self, task):
# #         if task in self.tasks:
# #             self.tasks.remove(task)
# #             print(f"Task removed: '{task}'")
# #         else:
# #             print(f"Task not found: '{task}'")
# #
# #     def list_tasks(self):
# #         if not self.tasks:
# #             print("No tasks available.")
# #         else:
# #             print("Current Tasks:")
# #             for  i in self.tasks:
# #                 print(f"{i}")
# #
# #
# # # Create an instance of the TaskManager
# # manager = TaskManager()
# #
# # # User input loop
# # while True:
# #     print("\n--- Task Manager ---")
# #     print("1. Add Task")
# #     print("2. Remove Task")
# #     print("3. List Tasks")
# #     print("4. Exit")
# #
# #     choice = input("Choose an option (1-4): ")
# #
# #     if choice == '1':
# #         task = input("Enter the task to add: ")
# #         manager.add_task(task)
# #
# #     elif choice == '2':
# #         task = input("Enter the task to remove: ")
# #         manager.remove_task(task)
# #
# #     elif choice == '3':
# #         manager.list_tasks()
# #
# #     elif choice == '4':
# #         print("Exiting Task Manager.")
# #         break
# #
# #     else:
# #         print("Invalid option. Please choose 1–4.")
