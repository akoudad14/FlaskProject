
from database.schema.EpisodeSchema import EpisodeSchema
from Service.RessourceService import RessourceService


class EpisodeService(RessourceService):

    @property
    def schema(self):
        return EpisodeSchema()

    def get_episodes(self) -> list:
        """Retrieves episodes from the database."""
        return self.dao.get_episodes()

    def get_episode(self, episode_id: int):
        return self.dao.get_episode(episode_id)
