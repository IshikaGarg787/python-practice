class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary  # Default salary for employees

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)  # Inherit base salary
        self.bonus = bonus  # Manager gets a bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus  # Salary includes bonus

class Developer(Employee):
    def __init__(self, name, base_salary, overtime_hours, overtime_rate):
        super().__init__(name, base_salary)  # Inherit base salary
        self.overtime_hours = overtime_hours
        self.overtime_rate = overtime_rate  # Developer gets paid for overtime

    def calculate_salary(self):
        overtime_pay = self.overtime_hours * self.overtime_rate
        return self.base_salary + overtime_pay  # Salary includes overtime pay

# Example usage
manager = Manager("Alice", 5000, 1000)
developer = Developer("Bob", 4000, 10, 20)

print(f"{manager.name}'s Salary: ${manager.calculate_salary()}")
print(f"{developer.name}'s Salary: ${developer.calculate_salary()}")
