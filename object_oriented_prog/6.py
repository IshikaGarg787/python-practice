class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        self.books.append(book)  # Add book to the list
        print(f"Added '{book.title}' by {book.author} to the library.")

    def remove_book(self, title):
        for book in self.books:  # Loop through books
            if book.title == title:
                self.books.remove(book)  # Remove the book
                print(f"Removed '{title}' from the library.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self, title):
        for book in self.books:  # Loop through books
            if book.title == title:
                print(f"Found: '{book.title}' by {book.author}")
                return
        print(f"Book '{title}' not found.")

# Example usage:
library = Library()

# Adding books
library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
library.add_book(Book("1984", "George Orwell"))

# Searching for a book
library.search_book("1984")

# Removing a book
library.remove_book("The Great Gatsby")
