
from database import ma
from database.models.Character import Character


class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Character

    comments = ma.Nested("CommentSchema", many=True, only=('id',))
    episodes = ma.Nested("EpisodeSchema", many=True, only=('id',))
