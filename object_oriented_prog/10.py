class ATM:
    def __init__(self, balance):
        self.balance = balance  # Store account balance

    def deposit(self, amount):
            self.balance += amount  # Add amount to balance
            print(f"Deposited: ${amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Transaction failed: Insufficient balance.")
        else:
            self.balance -= amount  # Deduct amount from balance
            print(f"Withdrew: ${amount}")

    def check_balance(self):
        print(f"Current Balance: ${self.balance}")

# Example usage:
atm = ATM(5000)  # Initialize ATM with $5000 balance

# Simulate ATM operations
atm.deposit(1500)
atm.withdraw(7000)  # Exceeds balance
atm.withdraw(1800)  # Valid transaction
atm.check_balance()
