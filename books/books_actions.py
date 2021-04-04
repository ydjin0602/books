from books.db_model import Book, session, BookSchema
from books.request_options import CreateBookOptions, UpdateBookOptions


def create_book(book: CreateBookOptions):
    book_object = Book(title=book.title, author=book.author, pages_num=book.pages_num)
    session.add(book_object)
    session.commit()

    book_schema = BookSchema().dump(book_object)
    return book_schema


def update_book(book: UpdateBookOptions):
    book_object = Book.query.get(book.id)

    book_object.title = book.title
    book_object.author = book.author
    book_object.pages_num = book.pages_num

    session.add(book_object)
    session.commit()

    book_schema = BookSchema().dump(book_object)
    return book_schema


def delete_book():
    pass


def get_book():
    pass


def get_all_books():
    pass
