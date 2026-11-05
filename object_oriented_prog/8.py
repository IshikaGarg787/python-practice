class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []  # List to store grades

    def add_grade(self, grade):
        if 0 <= grade <= 100:  # Ensuring the grade is valid
            self.grades.append(grade)
            print(f"Added grade: {grade}")
        else:
            print("Grade must be between 0 and 100.")

    def calculate_average(self):
        total = 0
        for grade in self.grades:  # Loop through grades
            total += grade
        return total / len(self.grades)  # Calculate average

# Example usage:
student = Student("Alice")

# Adding grades
student.add_grade(85)
student.add_grade(90)
student.add_grade(78)

# Calculating average grade
print(f"{student.name}'s Average Grade: {student.calculate_average():.2f}")
