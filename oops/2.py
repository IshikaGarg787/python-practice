class Student:
    def __init__(self, name, roll_number, course):
        self.name = name
        self.roll_number = roll_number
        self.course = course

    def display(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Course: {self.course}"


class StudentRecords:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        course = input("Enter course: ")
        student = Student(name, roll_number, course)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records available.")
        else:
            print("\nStudent Records:")
            for student in self.students:
                print(student.display())

    def search_student(self):
        roll_number = input("Enter roll number to search: ")
        found = False
        for student in self.students:
            if student.roll_number == roll_number:
                print("Student Found:")
                print(student.display())
                found = True
                break
        if not found:
            print("No student found with the given roll number.")

    def menu(self):
        while True:
            print("\nStudent Records Menu")
            print("1. Add Student")
            print("2. View All Students")
            print("3. Search for a Student")
            print("4. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                print("Exiting the Student Records system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Instantiate and run the menu
records = StudentRecords()
records.menu()
