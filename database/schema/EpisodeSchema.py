
from database import ma
from database.models.Episode import Episode


class EpisodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Episode

    characters = ma.Nested("CharacterSchema", many=True, only=('id', 'name'))

