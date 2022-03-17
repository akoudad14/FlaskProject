
from database import db
from database.models.ressource.CharacterEpisode import character_episode
from database.models.ressource.EspisodeComment import episode_comment


class Episode(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    air_date = db.Column(db.String)
    episode = db.Column(db.String)

    characters = db.relationship('Character', secondary=character_episode)
    comments = db.relationship('Comment', secondary=episode_comment)

