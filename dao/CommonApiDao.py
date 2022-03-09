
import abc


class ApiDao(abc.ABC):

    @property
    @abc.abstractmethod
    def model(self):
        pass

    @property
    @abc.abstractmethod
    def model_id(self):
        pass

    def get_all(self):
        return self.model.query.all()
