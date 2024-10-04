class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books_list = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                break

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.borrowed_books_list.append(book)
                self.books.remove(book)
                break

    def return_book(self, book_title):
        for book in self.borrowed_books_list:
            if book.title == book_title:
                self.books.append(book)
                self.borrowed_books_list.remove(book)
                break

    def available_books(self):
        return f'Available books : {[book.title for book in self.books]}'

    def borrowed_books(self):
        return f'Borrowed books : {[book.title for book in self.borrowed_books_list]}'


def main():
    books_data = [('baba à la plage', 'jacob', 1968),
                  ("L'avenir des autruches", 'Bobby', 2004),
                  ('le coût de la vie', 'fishers', 1995),
                  ('error_title', 'default', 0)]
    the_library = Library()
    for book in books_data:
        the_library.add_book(Book(book[0], book[1], book[2]))
    print('\n--- Library start ---')
    print(the_library.available_books())
    print(the_library.borrowed_books())

    the_library.remove_book('error_title')
    print("\n--- Library remove 'error_title' ---")
    print(the_library.available_books())
    print(the_library.borrowed_books())

    the_library.borrow_book('baba à la plage')
    print("\n--- Library borrow 'baba à la plage' ---")
    print(the_library.available_books())
    print(the_library.borrowed_books())

    the_library.return_book('baba à la plage')
    print("\n--- Library return 'baba à la plage' ---")
    print(the_library.available_books())
    print(the_library.borrowed_books())


if __name__ == '__main__':
    main()
