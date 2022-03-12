
from database import ma
from database.models.Character import Character


class CharacterSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Character

    episodes = ma.Nested("EpisodeSchema", many=True, only=('id', 'name'))
