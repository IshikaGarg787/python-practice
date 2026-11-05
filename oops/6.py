class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius

def main():
    while True:
        print("\nCalculate Area")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            rectangle = Rectangle(length, width)
            print(f"Area of Rectangle: {rectangle.area()}")

        elif choice == '2':
            radius = float(input("Enter the radius of the circle: "))
            circle = Circle(radius)
            print(f"Area of Circle: {circle.area()}")

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please enter a valid option.")

main()
