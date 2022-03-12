
from dao.CommentDao import CommentDao
from database.schema.CommentSchema import CommentSchema
from Service.ApiService import ApiService


class CommentService(ApiService):

    @property
    def dao(self):
        return CommentDao()

    @property
    def schema(self):
        return CommentSchema()
