import typing as t

import sqlalchemy as db
from marshmallow import Schema, fields
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///db.sqlite')
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()


class Book(Base):
    __tablename__ = 'books'
    __tableargs__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('title', db.String(20), nullable=False)
    author = db.Column('author', db.String(20), nullable=False)
    pages_num = db.Column('pages_num', db.Integer, nullable=False)

    def __init__(self, title: t.Text = '', author: t.Text = '', pages_num: int = 0):
        self.title = title
        self.author = author
        self.pages_num = pages_num

    def __repr__(self):
        return '<Book %r>' % self.title


class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    author = fields.Str()
    pages_num = fields.Int()
