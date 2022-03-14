
from database import db
from database.models.CharacterComment import character_comment
from database.models.EspisodeComment import episode_comment


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String)

    character = db.relationship('Character', secondary=character_comment)
    episode = db.relationship('Episode', secondary=episode_comment)
