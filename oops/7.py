class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks  # marks is a dictionary with subject names as keys and marks as values

    def calculate_grade(self):
        total_marks = sum(self.marks.values())
        average_marks = total_marks / len(self.marks)

        if average_marks >= 80:
            return 'A'
        elif average_marks >= 60:
            return 'B'
        elif average_marks >= 40:
            return 'C'
        else:
            return 'F'

    def display_student_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Subjects and Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")

# Example usage
students = []

student1 = Student("Alice", 101, {"Math": 85, "Physics": 78, "Chemistry": 88})
students.append(student1)

student2 = Student("Bob", 102, {"Math": 55, "Physics": 65, "Chemistry": 70})
students.append(student2)

student3 = Student("Charlie", 103, {"Math": 35, "Physics": 40, "Chemistry": 38})
students.append(student3)

for student in students:
    student.display_student_details()
    print()

