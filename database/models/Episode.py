
from database import db
from database.models.CharacterEpisode import character_episode
from database.models.EpisodeComment import episode_comment


class Episode(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    air_date = db.Column(db.String)
    episode = db.Column(db.String)

    comments = db.relationship('Comment', secondary=episode_comment,
                               backref='episode')
    characters = db.relationship('Character', secondary=character_episode)

