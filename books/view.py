import json
import logging
import typing as t
from http import HTTPStatus

from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError
from sqlalchemy import exc

from books.books_actions import create_book, update_book
from books.db_model import Book, BookSchema
from books.request_options import CreateBookOptions, UpdateBookOptions, DeleteBookOptions

LOGGER = logging.getLogger(__name__)


class BooksView(MethodView):
    __CREATE_BOOK_SCHEMA = CreateBookOptions.schema()
    __UPDATE_BOOK_SCHEMA = UpdateBookOptions.schema()
    __DELETE_BOOK_SCHEMA = DeleteBookOptions.schema()

    def get(self):
        book_id = 1
        print(Book.query.filter_by(id=book_id).first().id)
        return 'ok', 200

    def post(self):
        try:
            request_body: CreateBookOptions = self.__CREATE_BOOK_SCHEMA.load(request.json)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        try:
            book = create_book(request_body)
        except exc.SQLAlchemyError:
            return jsonify(
                {
                    'status': 'transaction error'
                }
            ), HTTPStatus.SERVICE_UNAVAILABLE

        return book

    def put(self):
        try:
            request_body = self.__UPDATE_BOOK_SCHEMA.load(request.json)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        try:
            book = update_book(request_body)
        except exc.SQLAlchemyError:
            return jsonify(
                {
                    'status': 'transaction error'
                }
            ), HTTPStatus.SERVICE_UNAVAILABLE

        return book

    def delete(self):
        try:
            request_body = self.__DELETE_BOOK_SCHEMA.load(request.json)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        return 'ok', 200

    @staticmethod
    def __return_bad_request(exception: t.Any):
        LOGGER.warning('Request body is invalid.', exc_info=exception)
        return jsonify(
            {
                'error': 'request body is invalid.'
            }
        ), HTTPStatus.BAD_REQUEST
