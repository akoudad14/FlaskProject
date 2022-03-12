
from database import ma
from database.models.Comment import Comment


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment

    character = ma.Nested("CharacterSchema", only=('id', 'name'))
    episode = ma.Nested("EpisodeSchema", only=('id', 'name'))
