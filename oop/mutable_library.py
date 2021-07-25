class Library:
    """Represent a library"""
    def __init__(self, books=None):
        if books:
            self.books = books
        else:
            self.books = []

    def add_books(self, book):
        """Add a book to the library"""
        self.books.append(book)


london = Library(['The Surrender'])
london.add_books('The Clean Coder')
london.add_books('War and Peace')
print(london.books)

new_york = Library()
new_york.add_books('The Power of Now')
print(new_york.books)