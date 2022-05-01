from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    published = db.Column(db.DateTime, nullable=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self) -> str:
        return '<News {} {}>'.format(self.title, self.url)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column()
    password = db.Column()
    role = db.Column()

    def set_password(self, password):
        pass

    def check_password(self, password):
        pass

    def __repr__(self) -> str:
        return '<User {0} id={1}>'.format(self.username, self.id)
