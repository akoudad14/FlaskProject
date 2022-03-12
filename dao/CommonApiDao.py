
import abc


class ApiDao(abc.ABC):

    @property
    @abc.abstractmethod
    def model(self):
        pass

    def get_all(self) -> list:
        """Function to get all specific objects in the database"""
        return self.model.query.all()
