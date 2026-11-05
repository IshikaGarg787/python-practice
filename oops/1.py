class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        isbn = input("Enter the ISBN number: ")
        book = Book(title, author, isbn)
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("\nBooks in the library:")
            for book in self.books:
                print(book.display())

    def search_book(self):
        search_term = input("Enter the title, author, or ISBN to search: ")
        results = [book for book in self.books if search_term.lower() in book.title.lower() \
                   or search_term.lower() in book.author.lower() or search_term == book.isbn]
        if results:
            print("\nSearch results:")
            for book in results:
                print(book.display())
        else:
            print("No matching books found.")

    def menu(self):
        while True:
            print("\nLibrary Menu")
            print("1. Add a Book")
            print("2. View All Books")
            print("3. Search for a Book")
            print("4. Exit")

            choice = input("Choose an option: ")
            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                print("Exiting the Library system. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

library = Library()
library.menu()
