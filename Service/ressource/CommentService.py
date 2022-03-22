
from Service.ressource.RessourceService import RessourceService


class CommentService(RessourceService):

    def get_comments(
            self,
            start: int = None,
            limit: int = None,
            **filters) -> list:
        """Retrieves characters from the database."""
        return self.dao.get_comments(start, limit, **filters)

    def add_comment(self, values):
        self.dao.insert_comment(**values)

    def get_comment(self, character_id: int):
        return self.dao.get_comment(character_id)

    def update_comment(self, comment_id: int, **kwargs):
        self.dao.update_comment(comment_id, **kwargs)

    def delete_comment(self, comment_id: int):
        self.dao.delete_comment(comment_id)
