class Employee:
    def __init__(self, name, department, age=30):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")

# Demonstrating constructor overloading
# Using the first constructor with all attributes
employee1 = Employee(name="Alice", department="HR", age=25)
employee1.display_info()

# Using the second constructor with default age
employee2 = Employee(name="Bob", department="IT")
employee2.display_info()
