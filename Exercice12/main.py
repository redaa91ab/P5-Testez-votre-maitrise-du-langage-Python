class Book:
    """ class that represent a book """
    def __init__(self, title, author, year):
        """
        Args :
            title : book's title
            author : book's author
            year : book's year
        """
        self.title = title
        self.author = author
        self.year = year

class Library:
    """ class that represent a library """
    def __init__(self):
        """
        Args :
            books : List of books available in the library
            borrowed_books :List of books borrowed
        """

        self.books = []
        self.borrowed_books = []

    def add_book(self, book) :
        """ Add the book object in self.books """
        self.books.append(book)

    def remove_book(self, book_title):
        """ Remove the book object from the title in self.books """
        for book in self.books :
            if book.title == book_title :
                self.books.remove(book)

    def borrow_book(self, book_title):
        """ Remove the book object in self.books and add it in self.borrowed_books """
        for book in self.books :
            if book.title == book_title :
                self.books.remove(book)
                self.borrowed_books.append(book)

    def return_book(self, book_title):
        """ Remove the book object in self.borrowed_books and add it in self.books """
        for book in self.borrowed_books :
            if book.title == book_title :
                self.borrowed_books.remove(book)
                self.books.append(book)

    def available_books(self):
        """ Return a list of titles of books available """
        all_books_title = [book.title for book in self.books]
        return all_books_title

    def get_borrowed_books(self):
        """ Return a list of titles of books borrowed """
        all_borrowed_books_title = [book.title for book in self.borrowed_books]
        return all_borrowed_books_title