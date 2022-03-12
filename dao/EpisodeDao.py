
from database.models.Episode import Episode
from dao.CommonApiDao import ApiDao


class EpisodeDao(ApiDao):

    @property
    def model(self):
        return Episode
