
from database import db
from database.models.CharacterComment import character_comment
from database.models.CharacterEpisode import character_episode


class Character(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    status = db.Column(db.String)
    species = db.Column(db.String)
    type = db.Column(db.String)
    gender = db.Column(db.String)

    comments = db.relationship('Comment', secondary=character_comment,
                               backref='character')
    episodes = db.relationship('Episode', secondary=character_episode)
