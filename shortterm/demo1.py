# Base Class
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}")


# Child Class
class GraduateStudent(Student):
    def __init__(self, student_id, name, course):
        super().__init__(student_id, name)
        self.course = course

    def display(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}")


# System Class
class StudentSystem:

    def __init__(self):
        self.students = {}   # dictionary to store students

    # Add student
    def add_student(self):
        try:
            student_id = input("Enter Student ID: ")

            if student_id in self.students:
                raise Exception("Student ID already exists")

            name = input("Enter Name: ")
            stype = input("Graduate student? (y/n): ")

            if stype.lower() == "y":
                course = input("Enter Course: ")
                student = GraduateStudent(student_id, name, course)
            else:
                student = Student(student_id, name)

            self.students[student_id] = student
            print("Student added successfully")

        except Exception as e:
            print("Error:", e)

    # Search student
    def search_student(self):
        student_id = input("Enter Student ID to search: ")

        if student_id in self.students:
            self.students[student_id].display()
        else:
            print("Student not found")

    # Delete student
    def delete_student(self):
        try:
            student_id = input("Enter Student ID to delete: ")

            if student_id not in self.students:
                raise Exception("Student does not exist")

            del self.students[student_id]
            print("Student deleted successfully")

        except Exception as e:
            print("Error:", e)

    # Show all students
    def show_students(self):
        if not self.students:
            print("No students available")
            return

        for student in self.students.values():
            student.display()


# Menu Program
system = StudentSystem()

while True:
    print("\nStudent Management System")
    print("1 Add Student")
    print("2 Search Student")
    print("3 Delete Student")
    print("4 Show All Students")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        system.add_student()

    elif choice == "2":
        system.search_student()

    elif choice == "3":
        system.delete_student()

    elif choice == "4":
        system.show_students()

    elif choice == "5":
        print("Program Ended")
        break

    else:
        print("Invalid choice")