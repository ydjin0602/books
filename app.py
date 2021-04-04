from flask import Flask
from books.view import BooksView
from books.db_model import Base, engine


app = Flask(__name__)
app.add_url_rule('/', view_func=BooksView.as_view(''))

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    app.run()
