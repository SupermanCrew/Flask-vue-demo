from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Guanli(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))


class Chushou(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 姓名
    username = db.Column(db.String(255),nullable=True,unique=True)
    # 密码
    password = db.Column(db.String(255),nullable=True)
    img_url = db.Column(db.String(255), nullable=True)
    # 简介
    jianjie = db.Column(db.String(255), default='房东', nullable=True)
    shouji = db.Column(db.String(255), default='18888888888')

# 家长
class Goumai(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # 姓名
    username = db.Column(db.String(255),nullable=True,unique=True)
    # 密码
    password = db.Column(db.String(255),nullable=True)
    img_url = db.Column(db.String(255), nullable=True)
    # 简介
    jianjie = db.Column(db.String(255),default='租客',nullable=True)
    shouji = db.Column(db.String(255), default='16666666666')


class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(255), nullable=False)
   img_url = db.Column(db.String(255), nullable=True)
   authors = db.relationship('Author', secondary='book_author', backref='books')
   publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)


book_author = db.Table(
    'book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)


class Author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255), nullable=False)


class Publisher(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(255), nullable=False)
   books = db.relationship('Book', backref='publisher')