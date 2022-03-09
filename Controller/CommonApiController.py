
import abc


class ApiController(abc.ABC):

    @property
    @abc.abstractmethod
    def service(self):
        pass

    def get_all(self):
        return self.service.get_all()
