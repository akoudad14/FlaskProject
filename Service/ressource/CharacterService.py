
from Service.ressource.RessourceService import RessourceService


class CharacterService(RessourceService):

    def get_characters(
            self,
            start: int = None,
            limit: int = None,
            **filters) -> list:
        """Retrieves characters from the database."""
        return self.dao.get_characters(start, limit, **filters)

    def get_character(self, character_id: int):
        return self.dao.get_character(character_id)
