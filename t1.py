class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"Successfully borrowed '{self.title}'!")

    def return_book(self):
        self.is_borrowed = False
        print(f"Successfully returned '{self.title}'!")

book1 = Book("1984", "George Orwell")
book2 = Book("The Hobbit", "J.R.R. Tolkien")
book3 = Book("To Kill a Mockingbird", "Harper Lee")

books = [book1, book2, book3]
for book in books:
    book.borrow()
    book.return_book()