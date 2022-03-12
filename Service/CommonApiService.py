
import abc


class ApiService(abc.ABC):

    @property
    @abc.abstractmethod
    def dao(self):
        pass

    @property
    @abc.abstractmethod
    def schema(self):
        pass

    def get_all(self) -> list:
        """Function to get all specific objects in the database."""
        objects = self.dao.get_all()
        return [self.schema.dump(obj) for obj in objects]
