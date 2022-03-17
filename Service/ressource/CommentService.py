
from database.schema.CommentSchema import CommentSchema
from Service.ressource.RessourceService import RessourceService


class CommentService(RessourceService):

    @property
    def schema(self):
        return CommentSchema()

    def get_comments(
            self,
            start: int = None,
            limit: int = None,
            **filters) -> list:
        """Retrieves characters from the database."""
        objects = self.dao.get_comments(start, limit, **filters)
        return [self.schema.dump(obj) for obj in objects]

    def add_comment(self, values):
        self.dao.insert_comment(**values)

    def get_comment(self, character_id: int):
        return self.dao.get_comment(character_id)

    def update_comment(self, comment_id: int, **kwargs):
        self.dao.update_comment(comment_id, **kwargs)

    def delete_comment(self, comment_id: int):
        self.dao.delete_comment(comment_id)
