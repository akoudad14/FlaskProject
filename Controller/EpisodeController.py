
from Controller.CommonApiController import ApiController
from Service.EpisodeService import EpisodeService


class EpisodeController(ApiController):

    @property
    def service(self) -> EpisodeService:
        return EpisodeService()
