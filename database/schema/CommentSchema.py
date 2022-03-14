
from database import ma
from database.models.Comment import Comment


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment

    character = ma.Nested("CharacterSchema", many=True, only=('id',))
    episode = ma.Nested("EpisodeSchema", many=True, only=('id',))
