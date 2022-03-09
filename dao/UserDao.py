
from database.models.User import User
from dao.CommonApiDao import ApiDao


class UserDao(ApiDao):

    @property
    def model(self):
        return User
