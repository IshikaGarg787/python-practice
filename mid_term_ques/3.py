class BankAccount:
    def __init__(self, initial_balance):
        # Initialize balance as a private attribute
        self.initial_balance = initial_balance  

    def deposit(self, amount):
        # Add amount to balance
        self.initial_balance += amount  

    def withdraw(self, amount):
        # Subtract from balance but prevent overdraft
        if amount <= self.initial_balance:
            self.initial_balance -= amount  

    def get_balance(self):
        # Return the current balance
        return self.initial_balance  

# Test Input
acc = BankAccount(100)
acc.deposit(50)   # 100 + 50 = 150
acc.withdraw(30)  # 150 - 30 = 120
print(acc.get_balance())  # Expected Output: 120
