
import abc
from Service.CommonApiService import ApiService


class ApiController(abc.ABC):

    @property
    @abc.abstractmethod
    def service(self) -> ApiService:
        pass

    def get_all(self) -> list:
        """Function to get all specific objects in the database"""
        return self.service.get_all()
