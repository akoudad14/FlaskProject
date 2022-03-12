
from dao.CommonApiDao import ApiDao
from database.models.Episode import Episode


class EpisodeDao(ApiDao):

    @property
    def model(self):
        return Episode
