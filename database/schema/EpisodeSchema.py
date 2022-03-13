
from database import ma
from database.models.Episode import Episode


class EpisodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Episode

    comments = ma.Nested("Comment", many=True)
    characters = ma.Nested("CharacterSchema", many=True, only=('id', 'name'))

