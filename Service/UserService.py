
from dao.UserDao import UserDao
from database.schema.UserSchema import UserSchema
from Service.CommonApiService import ApiService


class UserService(ApiService):

    @property
    def dao(self):
        return UserDao()

    @property
    def schema(self):
        return UserSchema()
