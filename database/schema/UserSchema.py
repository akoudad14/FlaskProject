
from database import ma
from database.models.User import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        exclude = ('password', 'favorite_place_id', 'creation_date', 'deactivated_date',)
