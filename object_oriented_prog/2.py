class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.items = []  # List to store items

    def add_item(self, name, price):
        self.items.append(Item(name, price))  # Create Item and add to cart
        print(f"Added {name} (${price}) to the cart.")

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                print(f"Removed {name} from the cart.")
                return
        print(f"Item '{name}' not found.")

    def total_price(self):
        return sum(item.price for item in self.items)

# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 1.5)
cart.add_item("Bread", 2.0)
cart.remove_item("Apple")
print(f"Total price: ${cart.total_price()}")

