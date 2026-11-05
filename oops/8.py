class BankAccount:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Withdrawal amount must be greater than 0.")

    def display_account_details(self):
        print(f"Account holder: {self.name}")
        print(f"Account balance: {self.balance}")


# Create a dictionary to store accounts
accounts = {}

# Menu loop
while True:
    print("\n--- Bank Menu ---")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':  # Create Account
        name = input("Enter account holder's name: ")
        initial_deposit = float(input("Enter initial deposit amount: "))
        account = BankAccount(name, initial_deposit)
        accounts[name] = account
        print("Account created successfully!")

    elif choice == '2':  # Deposit Money
        name = input("Enter account holder's name: ")
        if name in accounts:
            amount = float(input("Enter deposit amount: "))
            accounts[name].deposit(amount)
        else:
            print("Account not found.")

    elif choice == '3':  # Withdraw Money
        name = input("Enter account holder's name: ")
        if name in accounts:
            amount = float(input("Enter withdrawal amount: "))
            accounts[name].withdraw(amount)
        else:
            print("Account not found.")

    elif choice == '4':  # Display Account Details
        name = input("Enter account holder's name: ")
        if name in accounts:
            accounts[name].display_account_details()
        else:
            print("Account not found.")

    elif choice == '5':  # Exit
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
