
from dao.CharacterDao import CharacterDao
from database.schema.CharacterSchema import CharacterSchema
from Service.CommonApiService import ApiService


class CharacterService(ApiService):

    @property
    def dao(self):
        return CharacterDao()

    @property
    def schema(self):
        return CharacterSchema()
