
import abc


class ApiController(abc.ABC):

    @property
    @abc.abstractmethod
    def service(self):
        pass

    def get_all(self):
        """Function to get all specific objects in the database"""
        return self.service.get_all()
