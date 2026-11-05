class Employee:
    def __init__(self, name, salary):
        self.__name = name      # Private attribute
        self.__salary = salary  # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for salary
    def get_salary(self):
        return self.__salary

    # Setter for salary (with validation)
    def set_salary(self, salary):
        if salary >= 0:  # Ensure salary is non-negative
            self.__salary = salary
        else:
            print("Salary cannot be negative.")

# Example usage:
emp = Employee("Alice", 5000)

# Access using getters
print(f"Employee Name: {emp.get_name()}")
print(f"Employee Salary: ${emp.get_salary()}")

# Modify using setters
emp.set_name("Bob")
emp.set_salary(5500)

# Display updated details
print(f"Updated Employee Name: {emp.get_name()}")
print(f"Updated Employee Salary: ${emp.get_salary()}")
