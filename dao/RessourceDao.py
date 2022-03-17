
import abc

from database import db
from database.models.ressource.Character import Character
from database.models.ressource.Comment import Comment
from database.models.ressource.Episode import Episode


class RessourceDao(abc.ABC):

    def get_characters(
            self,
            page: int = None,
            page_size: int = None,
            **filters) -> list:
        """Retrieves characters from the database."""
        query = Character.query
        if 'episode_ids' in filters:
            episode_ids = filters.pop('episode_ids')
            query = query.join(Character.episodes)\
                .filter(Episode.id.in_(episode_ids))
        if 'comment_ids' in filters:
            comment_ids = filters.pop('comment_ids')
            query = query.join(Character.comments) \
                .filter(Comment.id.in_(comment_ids))
        query = query.filter_by(**filters)
        if page_size:
            query = query.limit(page_size)
            if page:
                query = query.offset(page * page_size)
        return query.all()

    def get_character(self, character_id: int):
        return Character.query\
            .filter(Character.id == character_id).first_or_404()

    def get_episodes(self) -> list:
        """Retrieves episodes from the database."""
        return Episode.query.all()

    def get_episode(self, episode_id: int):
        return Episode.query.filter(Episode.id == episode_id).first_or_404()

    def get_comments(
            self,
            page: int = None,
            page_size: int = None,
            **filters) -> list:
        """Retrieves comments from the database."""
        query = Comment.query
        if 'episode_ids' in filters:
            episode_ids = filters.pop('episode_ids')
            query = query.join(Comment.episodes) \
                .filter(Episode.id.in_(episode_ids))
        if 'character_ids' in filters:
            character_ids = filters.pop('character_ids')
            query = query.join(Comment.characters) \
                .filter(Character.id.in_(character_ids))
        query = query.filter_by(**filters)
        if page_size:
            query = query.limit(page_size)
            if page:
                query = query.offset(page * page_size)
        return query.all()

    def get_comment(self, comment_id: int):
        return Comment.query.filter(Comment.id == comment_id).first_or_404()

    def insert_comment(self, **values):
        new = Comment(**values)
        db.session.add(new)
        db.session.commit()

    def update_comment(self, comment_id: int, **kwargs):
        obj = self.get_comment(comment_id)
        for attr, value in kwargs.items():
            obj.__setattr__(attr, value)
        db.session.commit()

    def delete_comment(self, comment_id: int):
        obj = self.get_comment(comment_id)
        db.session.delete(obj)
        db.session.commit()
