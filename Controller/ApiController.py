
import abc

from Service.CharacterService import CharacterService
from Service.CommentService import CommentService
from Service.EpisodeService import EpisodeService


class ApiController(abc.ABC):

    def get_all_characters(self) -> list:
        """Retrieves all characters from the database."""
        character_service = CharacterService()
        return character_service.get_all()

    def get_all_episodes(self) -> list:
        """Retrieves all episodes from the database."""
        episode_service = EpisodeService()
        return episode_service.get_all()

    def get_all_comments(self) -> list:
        """Retrieves all comments from the database."""
        comment_service = CommentService()
        return comment_service.get_all()

    def add_comment(self, comment_dict) -> bool:
        comment_service = CommentService()
        comment_service.insert(comment_dict)
        return True
