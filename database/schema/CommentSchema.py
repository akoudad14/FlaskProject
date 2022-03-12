
from database import ma
from database.models.Comment import Comment


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
