class PaymentMethod:
    def pay(self, amount):
        pass  # Abstract method placeholder

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class DebitCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Debit Card.")

class Cash(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} in Cash.")

# Example usage:
amount = int(input("Enter amount to pay: "))

# Creating instances of each payment method
credit = CreditCard()
debit = DebitCard()
cash = Cash()

# Calling the pay method for each payment type
credit.pay(amount)
debit.pay(amount)
cash.pay(amount)
