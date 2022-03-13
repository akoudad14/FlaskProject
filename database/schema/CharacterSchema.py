
from database import ma
from database.models.Character import Character


class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Character

    comments = ma.Nested("Comment", many=True)
    episodes = ma.Nested("EpisodeSchema", many=True, only=('id', 'name'))
