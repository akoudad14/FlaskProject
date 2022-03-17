
from database import db

character_comment = db.Table('character_comment', db.metadata,
                             db.Column('character_id', db.Integer,
                                       db.ForeignKey('character.id')),
                             db.Column('comment_id', db.Integer,
                                       db.ForeignKey('comment.id')))
