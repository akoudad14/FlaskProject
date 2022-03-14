
from database import db

character_episode_comment = \
    db.Table('character_episode_comment',
             db.metadata,
             db.Column('character_episode_id', db.Integer,
                       db.ForeignKey('character_episode.id')),
             db.Column('comment_id', db.Integer,
                       db.ForeignKey('comment.id')))
