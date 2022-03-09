
from Controller.CommonApiController import ApiController
from Service.UserService import UserService


class UserController(ApiController):
    
    @property
    def service(self):
        return UserService()
