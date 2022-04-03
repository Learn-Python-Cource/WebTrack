from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=True)
    url = db.Column(db.String, nullable=True)
    published = db.Column(db.DateTime, nullable=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<News {} {}>'.format(self.title, self.url)
