
import abc

from database.schema.CharacterSchema import CharacterSchema
from database.schema.CommentSchema import CommentSchema
from database.schema.EpisodeSchema import EpisodeSchema
from Service.CharacterService import CharacterService
from Service.CommentService import CommentService
from Service.EpisodeService import EpisodeService


class RessourceController(abc.ABC):

    def get_characters(
            self,
            start: int = None,
            limit: int = None,
            **filters) -> list:
        """Retrieves characters from the database."""
        character_service = CharacterService()
        character_schema = CharacterSchema()
        characters = character_service.get_characters(start, limit, **filters)
        return [character_schema.dump(character) for character in characters]

    def get_episodes(self) -> list:
        """Retrieves episodes from the database."""
        episode_service = EpisodeService()
        episode_schema = EpisodeSchema()
        episodes = episode_service.get_episodes()
        return [episode_schema.dump(episode) for episode in episodes]

    def get_comments(
            self,
            start: int = None,
            limit: int = None,
            **filters) -> list:
        """Retrieves all comments from the database."""
        comment_service = CommentService()
        comment_schema = CommentSchema()
        comments = comment_service.get_comments(start, limit, **filters)
        return [comment_schema.dump(comment) for comment in comments]

    def add_comment(self, values: dict):
        comment_service = CommentService()
        if 'character_id' in values:
            character_id = values.pop('character_id')
            character_service = CharacterService()
            character = character_service.get_character(character_id)
            values['characters'] = [character]
        if 'episode_id' in values:
            episode_id = values.pop('episode_id')
            episode_service = EpisodeService()
            episode = episode_service.get_episode(episode_id)
            values['episodes'] = [episode]
        comment_service.add_comment(values)

    def get_comment(self, comment_id: int) -> str:
        comment_service = CommentService()
        comment_schema = CommentSchema()
        comment = comment_service.get_comment(comment_id)
        return comment_schema.dump(comment)

    def update_comment(self, comment_id: int, values: dict):
        comment_service = CommentService()
        comment_service.update_comment(comment_id, **values)

    def delete_comment(self, comment_id: int):
        comment_service = CommentService()
        comment_service.delete_comment(comment_id)
