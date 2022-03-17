
from database import db
from database.models.ressource.CharacterComment import character_comment
from database.models.ressource.EspisodeComment import episode_comment


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String)

    characters = db.relationship('Character', secondary=character_comment,
                                 lazy='dynamic')
    episodes = db.relationship('Episode', secondary=episode_comment,
                               lazy='dynamic')
