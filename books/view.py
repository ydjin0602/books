import json
import logging
import typing as t
from http import HTTPStatus

from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from sqlalchemy import exc

from books.book_actions import create_book, update_book, delete_book, get_book, get_all_books
from books.exception import BookNotFoundError
from books.request_options import CreateBookOptions, UpdateBookOptions, DeleteBookOptions, GetBookOptions

LOGGER = logging.getLogger(__name__)


class BooksView(MethodView):
    __GET_BOOK_SCHEMA = GetBookOptions.schema()
    __CREATE_BOOK_SCHEMA = CreateBookOptions.schema()
    __UPDATE_BOOK_SCHEMA = UpdateBookOptions.schema()
    __DELETE_BOOK_SCHEMA = DeleteBookOptions.schema()

    def get(self) -> [t.Dict[str, t.Any], HTTPStatus]:
        try:
            request_body: GetBookOptions = self.__GET_BOOK_SCHEMA.load(request.args.to_dict())
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        try:
            if request_body.id == 'all_books':
                books = get_all_books()
                return jsonify(
                    {
                        'result': books
                    }
                )
            else:
                book = get_book(request_body)
                return book
        except BookNotFoundError as exception:
            return self.__return_not_found_error(exception)
        except exc.SQLAlchemyError as exception:
            return self.__return_transaction_error(exception)

    def post(self) -> [t.Dict[str, t.Any], HTTPStatus]:
        try:
            request_body: CreateBookOptions = self.__CREATE_BOOK_SCHEMA.load(request.json)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        try:
            book = create_book(request_body)
        except exc.SQLAlchemyError as exception:
            return self.__return_transaction_error(exception)

        return book

    def put(self) -> [t.Dict[str, t.Any], HTTPStatus]:
        try:
            request_body: UpdateBookOptions = self.__UPDATE_BOOK_SCHEMA.load(request.json)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        try:
            book = update_book(request_body)
        except exc.SQLAlchemyError as exception:
            return self.__return_transaction_error(exception)

        return book

    def delete(self) -> [t.Dict[str, t.Any], HTTPStatus]:
        try:
            request_body: DeleteBookOptions = self.__DELETE_BOOK_SCHEMA.load(request.json)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        try:
            delete_book(request_body)
            return jsonify(
                {
                    'id': request_body.id,
                    'result': 'Book successfully deleted.'
                }
            )
        except BookNotFoundError as exception:
            return self.__return_not_found_error(exception)
        except exc.SQLAlchemyError as exception:
            return self.__return_transaction_error(exception)

    @staticmethod
    def __return_bad_request(exception: t.Any):
        LOGGER.warning('Request body is invalid.', exc_info=exception)
        return jsonify(
            {
                'error': 'request body is invalid.'
            }
        ), HTTPStatus.BAD_REQUEST

    @staticmethod
    def __return_transaction_error(exception: t.Any):
        LOGGER.warning('Transaction error.', exc_info=exception)
        return jsonify(
                {
                    'error': 'transaction error'
                }
            ), HTTPStatus.SERVICE_UNAVAILABLE

    @staticmethod
    def __return_not_found_error(exception: t.Any):
        LOGGER.warning("Book not found.", exc_info=exception)
        return jsonify(
            {
                'error': str(exception)
            }
        ), HTTPStatus.NOT_FOUND

