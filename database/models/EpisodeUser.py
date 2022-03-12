
from database import db

episode_user = db.Table('episode_user', db.metadata,
                        db.Column('user_id', db.Integer,
                                  db.ForeignKey('user.id')),
                        db.Column('episode_id', db.Integer,
                                  db.ForeignKey('episode.id')))
