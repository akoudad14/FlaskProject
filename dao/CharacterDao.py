
from dao.CommonApiDao import ApiDao
from database.models.Character import Character


class CharacterDao(ApiDao):

    @property
    def model(self):
        return Character
