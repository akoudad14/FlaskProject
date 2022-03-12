
from database import ma
from database.models.Episode import Episode


class EpisodeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Episode
