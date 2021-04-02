import json
import logging
import typing as t
from http import HTTPStatus

from flask import request, jsonify
from flask.views import MethodView
from marshmallow import ValidationError

from books.request_options import CreateBookOptions, UpdateBookOptions, DeleteBookOptions

LOGGER = logging.getLogger(__name__)


class BooksView(MethodView):
    __CREATE_BOOK_SCHEMA = CreateBookOptions.schema()
    __UPDATE_BOOK_SCHEMA = UpdateBookOptions.schema()
    __DELETE_BOOK_SCHEMA = DeleteBookOptions.schema()

    def get(self):
        pass

    def post(self):
        try:
            request_body = self.__CREATE_BOOK_SCHEMA.load(request.json)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        return 'ok', 200

    def put(self):
        try:
            request_body = self.__UPDATE_BOOK_SCHEMA.load(request.json)
        except (json.JSONDecodeError, KeyError, UnicodeDecodeError, ValidationError) as exception:
            return self.__return_bad_request(exception)

        return 'ok', 200

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
