
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

    def add_comment(self, comment_dict):
        comment_service = CommentService()
        comment_service.insert(comment_dict)

    def get_one_comment(self, comment_id: int) -> str:
        comment_service = CommentService()
        return comment_service.get_one(comment_id)

    def update_comment(self, comment_id: int, comment_dict: dict):
        comment_service = CommentService()
        comment_service.update(comment_id, **comment_dict)

    def delete_comment(self, comment_id: int):
        comment_service = CommentService()
        comment_service.delete(comment_id)
