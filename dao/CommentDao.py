
from dao.ApiDao import ApiDao
from database.models.Comment import Comment


class CommentDao(ApiDao):

    @property
    def model(self):
        return Comment
