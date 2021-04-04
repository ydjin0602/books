import typing as t

from books.db_model import Book, session, BookSchema
from books.exception import BookNotFoundError
from books.request_options import CreateBookOptions, UpdateBookOptions, DeleteBookOptions, GetBookOptions


def create_book(book: CreateBookOptions) -> t.Dict[str, t.Any]:
    book_object = Book(title=book.title, author=book.author, pages_num=book.pages_num)
    session.add(book_object)
    session.commit()

    book_schema = BookSchema().dump(book_object)
    return book_schema


def update_book(book: UpdateBookOptions) -> t.Dict[str, t.Any]:
    book_object = Book.query.get(book.id)

    book_object.title = book.title
    book_object.author = book.author
    book_object.pages_num = book.pages_num

    session.add(book_object)
    session.commit()

    book_schema = BookSchema().dump(book_object)
    return book_schema


def delete_book(book: DeleteBookOptions) -> None:
    book_object = Book.query.get(book.id)
    session.delete(book_object)
    session.commit()


def get_book(book: GetBookOptions):
    book_object = Book.query.get(book.id)
    if not book_object:
        raise BookNotFoundError()
    book_schema = BookSchema().dump(book_object)
    return book_schema


def get_all_books():
    book_objects = Book.query.all()
    book_schemas = [BookSchema().dump(book) for book in book_objects]
    return book_schemas
