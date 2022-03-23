

from database.schema.UserSchema import UserSchema
from Service.UserService import UserService


class UserController:

    def get_users(self) -> list:
        """Retrieves all users from the database."""
        service = UserService()
        schema = UserSchema()
        comments = service.get_users()
        return [schema.dump(comment) for comment in comments]

    def get_user(self, user_id):
        service = UserService()
        schema = UserSchema()
        user = service.get_user(user_id)
        return schema.dump(user)

    def get_user_by_filter(self, dump=False, **kwargs):
        service = UserService()
        user = service.get_user_by_filter(**kwargs)
        if not user:
            return None
        if dump is False:
            return user
        schema = UserSchema()
        return schema.dump(user)

    def add_user(self, **kwargs):
        service = UserService()
        service.add_user(**kwargs)

    def update_user(self, user_id: int, values: dict):
        service = UserService()
        service.update_user(user_id, **values)

    def delete_user(self, user_id: int):
        service = UserService()
        service.delete_user(user_id)
