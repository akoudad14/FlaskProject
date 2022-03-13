
from database import db
from database.models.CharacterEpisodeComment import character_episode_comment


class Comment(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String)
