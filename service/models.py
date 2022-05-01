from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    published = db.Column(db.DateTime, nullable=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self) -> str:
        return '<News {0} {1}>'.format(self.title, self.url)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)  # noqa: WPS432
    password = db.Column(db.String(128))  # noqa: WPS432
    role = db.Column(db.String(10), index=True)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def insert_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return '<User {0} id={1}>'.format(self.username, self.id)
