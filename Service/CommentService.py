
from dao.CommentDao import CommentDao
from database.schema.CommentSchema import CommentSchema
from Service.CommonApiService import ApiService


class CommentService(ApiService):

    @property
    def dao(self):
        return CommentDao()

    @property
    def schema(self):
        return CommentSchema()

    def insert(self, comment_dict) -> bool:
        return self.dao.insert(**comment_dict)
