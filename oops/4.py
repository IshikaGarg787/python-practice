class Car:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price

    def display_info(self):
        print(f"Model: {self.model}, Brand: {self.brand}, Price: {self.price}")


class CarShowroom:
    def __init__(self):
        self.cars = []

    def add_car(self):
        model = input("Enter car model: ")
        brand = input("Enter car brand: ")
        price = input("Enter car price: ")
        car = Car(model, brand, price)
        self.cars.append(car)
        print("Car added successfully!")

    def display_cars(self):
        if not self.cars:
            print("No cars in the showroom.")
        else:
            print("\nCars in the showroom:")
            for car in self.cars:
                car.display_info()

    def menu(self):
        while True:
            print("\nCar Showroom Menu")
            print("1. Add Car")
            print("2. View All Cars")
            print("3. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_car()
            elif choice == "2":
                self.display_cars()
            elif choice == "3":
                print("Exiting the Car Showroom system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


# Instantiate and run the menu
showroom = CarShowroom()
showroom.menu()
