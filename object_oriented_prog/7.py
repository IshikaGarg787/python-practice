class Order:
    def __init__(self):
        self.products = []  # List to store (product, price) tuples

    def add_product(self, product, price):
            self.products.append((product, price))  # Store product as tuple
            print(f"Added '{product}' - ${price}")

    def remove_product(self, product):
        for item in self.products:  # Loop through products
            if item[0] == product:
                self.products.remove(item)  # Remove the first matching product
                print(f"Removed '{product}' from the order.")
                return
        print(f"Product '{product}' not found.")

    def calculate_total(self):
        total = 0
        for item in self.products:  # Loop through product list
            total += item[1]  # Sum up prices
        return total

# Example usage:
order = Order()

# Adding products
order.add_product("Laptop", 1000)
order.add_product("Mouse", 50)

# Removing a product
order.remove_product("Mouse")

# Calculating total price
print(f"Total Order Price: ${order.calculate_total()}")
