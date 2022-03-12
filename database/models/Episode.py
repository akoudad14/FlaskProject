
from database import db


class Episode(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    air_date = db.Column(db.String)
    episode = db.Column(db.String)
