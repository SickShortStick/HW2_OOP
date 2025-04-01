
class Book:
    
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.status = 'Available'
    
    def borrow(self):
        if self.status:
            self.status = 'Borrowed'

    def return_book(self):
        self.status = 'Available'

    def get_details(self):
        return f'{self.title} by {self.author} ({self.status})\n'

class Library:
    
    books = dict()
    
    def add_book(self, book: Book):
        Library.books[book.title] = book
        return f'Added {book.title} by {book.author}'
    
    def borrow_book(self, title: str):
        book : Book = Library.books[title]
        book.borrow()
        return f'Borrowed {book.title}'
    
    def return_book(self, title: str):
        book : Book = Library.books[title]
        book.return_book()
        return f'Returned {book.title}'

    def show_books(self, ):
        result = ''
        for book in list(Library.books.values()):
            result += '      ' + book.get_details()
        return result


library = Library()

splited_line = list(input().split('"'))
while splited_line[0].lower() != 'exit':
    match splited_line[0]:
        case 'ADD ':
            book = Book(splited_line[1], splited_line[3])
            print(library.add_book(book))
        case 'BORROW ':
            print(library.borrow_book(splited_line[1]))
        case 'RETURN ':
            print(library.return_book(splited_line[1]))
        case 'SHOW':
            print(library.show_books())
    splited_line = list(input().split('"'))
