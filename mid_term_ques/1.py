class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []  # List to store (credit, grade)

    def add_course(self, credit, grade):
        self.courses.append((credit, grade))  # Add course details

    def calculate_gpa(self):
        # Step 1: Define grade values
        grade_mapping = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

        total_points = 0  # To store total weighted grade points
        total_credits = 0  # To store total credits

        # Step 2: Loop through each course
        for credit, grade in self.courses:
            total_points += credit * grade_mapping[grade]  # Multiply credit by grade value
            total_credits += credit  # Add to total credits

        # Step 3: Calculate GPA (avoid division by zero)
        if total_credits == 0:
            return 0.0  # No courses, so GPA is 0.0
        
        return total_points / total_credits  # Divide total points by total credits

# Test the code
student = Student("Alice")
student.add_course(3, 'A')  # 3 credits, grade A (4.0)
student.add_course(4, 'B')  # 4 credits, grade B (3.0)
print(f"{student.calculate_gpa():.2f}")  # Expected Output: 3.14
