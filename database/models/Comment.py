
from database import db


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String)
