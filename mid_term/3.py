class BankAccount:
    def __init__(self, initial_balance):
       self.initial_balance = initial_balance
       self.amount = amount

    def deposit(self, amount):
       
    
    def withdraw(self, amount):
        # Subtract from balance (no overdraft)
        pass
    
    # Implement this
    def get_balance(self):
        pass

# Test Input
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())  # Expected Output: 120