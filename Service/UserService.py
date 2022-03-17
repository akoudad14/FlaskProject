
from dao.UserDao import UserDao
from database.schema.UserSchema import UserSchema


class UserService:

    def __init__(self):
        self.dao = UserDao()
        self.schema = UserSchema()

    def get_users(self) -> list:
        """Retrieves characters from the database."""
        objects = self.dao.get_users()
        return [self.schema.dump(obj) for obj in objects]

    def add_user(self, **values):
        self.dao.add_user(**values)

    def get_user(self, character_id: int):
        return self.dao.get_user(character_id)

    def get_user_by_filter(self, **kwargs):
        return self.dao.get_user_by_filter(**kwargs)

    def update_user(self, user_id: int, **kwargs):
        self.dao.update_user(user_id, **kwargs)

    def delete_user(self, user_id: int):
        self.dao.delete_user(user_id)
