
from database.schema.CharacterSchema import CharacterSchema
from Service.RessourceService import RessourceService


class CharacterService(RessourceService):

    @property
    def schema(self):
        return CharacterSchema()

    def get_characters(
            self,
            start: int = None,
            limit: int = None,
            **filters) -> list:
        """Retrieves characters from the database."""
        return self.dao.get_characters(start, limit, **filters)

    def get_character(self, character_id: int):
        return self.dao.get_character(character_id)
