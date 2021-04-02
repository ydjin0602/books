from flask import Flask

from books.view import BooksView


app = Flask(__name__)
app.add_url_rule('/', view_func=BooksView.as_view(''))


if __name__ == '__main__':
    app.run()
