
from database import db

episode_comment = db.Table('episode_comment', db.metadata,
                           db.Column('episode_id', db.Integer,
                                     db.ForeignKey('episode.id')),
                           db.Column('comment_id', db.Integer,
                                     db.ForeignKey('comment.id')))
