
from Controller.CommonApiController import ApiController
from Service.CharacterService import CharacterService


class CharacterController(ApiController):
    
    @property
    def service(self) -> CharacterService:
        return CharacterService()
