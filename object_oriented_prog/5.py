class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if  amount <= self.balance:  
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def display_balance(self):
        print(f"Account {self.account_number} - Balance: ${self.balance}")

# Example usage:
account = BankAccount("123456789", 1000)

account.display_balance()  # Show initial balance
account.deposit(500)  # Deposit money
account.withdraw(300)  # Withdraw money
account.withdraw(1500) # Invalid withdrawal (insufficient funds)
account.display_balance()  # Show final balance
