
import abc


class ApiDao(abc.ABC):

    @property
    @abc.abstractmethod
    def model(self):
        pass

    def get_all(self) -> list:
        """Retrieves all specific objects from the database."""
        return self.model.query.all()
