class Vehicle:
    def __init__(self, brand):
        self.brand = brand  # Store brand name

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}")

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)  # Call parent constructor
        self.doors = doors  # Store number of doors

    def display_info(self):
        print(f"Car Brand: {self.brand}, Doors: {self.doors}")

class Bike(Vehicle):
    def __init__(self, brand, type):
        super().__init__(brand)  # Call parent constructor
        self.type = type  # Store bike type (e.g., mountain, road)

    def display_info(self):
        print(f"Bike Brand: {self.brand}, Type: {self.type}")

# Example usage:
car = Car("Toyota", 4)
bike = Bike("Yamaha", "Sports")

# Display information
car.display_info()
bike.display_info()
