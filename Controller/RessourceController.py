
import abc
import csv
from io import StringIO

from database.schema.CharacterSchema import CharacterSchema
from database.schema.CommentSchema import CommentSchema
from database.schema.EpisodeSchema import EpisodeSchema
from Service.ressource.CharacterService import CharacterService
from Service.ressource.CommentService import CommentService
from Service.ressource.EpisodeService import EpisodeService


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

    def get_comments_csv(self):
        """Retrieves all comments from the database."""
        comments = self.get_comments()
        si = StringIO()
        cw = csv.writer(si)
        lines = []
        lines.append(['id', 'comment', 'character_id', 'episode_id'])
        for comment in comments:
            line = [comment['id'], comment['comment'], comment['character']['id'],
                    comment['episode']['id']]
            lines.append(line)
        cw.writerows(lines)
        return si

    def add_comment(self, values: dict):
        comment_service = CommentService()
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
