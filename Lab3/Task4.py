class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' is currently not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You have returned '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' is already available.")

    def check_availability(self):
        if self.available:
            print(f"'{self.title}' by {self.author} is available.")
        else:
            print(f"'{self.title}' by {self.author} is currently not available.")

# Example usage:
book1 = Book("The ABC", "Ali")
book2 = Book("Hellow World", "Zain")

book1.check_availability()  # Check availability of book1
book1.borrow()              # Borrow book1
book1.borrow()              # Try to borrow book1 again (already borrowed)
book1.return_book()         # Return book1
book1.return_book()         # Try to return book1 again (already returned)

book2.check_availability()  # Check availability of book2
book2.borrow()              # Borrow book2
book2.return_book()         # Return book2
book2.check_availability()  # Check availability of book2 again
