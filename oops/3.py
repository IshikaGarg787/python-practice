class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def display_info(self):
        print("\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"Designation: {self.designation}")
        print(f"Salary: ${self.salary:.2f}")

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated to: ${self.salary:.2f}")

    def promote(self, new_designation):
        self.designation = new_designation
        print(f"Designation updated to: {self.designation}")


# Example usage
employee1 = Employee("Alice Johnson", "Software Developer", 70000)
employee2 = Employee("Bob Smith", "Data Scientist", 80000)

# Display information
employee1.display_info()
employee2.display_info()

# Update salary
employee1.update_salary(75000)

# Promote employee
employee2.promote("Senior Data Scientist")

# Display updated information
employee1.display_info()
employee2.display_info()
