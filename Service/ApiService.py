
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
        """Retrieves all specific objects from the database."""
        objects = self.dao.get_all()
        return [self.schema.dump(obj) for obj in objects]

    def insert(self, comment_dict):
        self.dao.insert(**comment_dict)

    def get_one(self, obj_id):
        obj = self.dao.get_one(obj_id)
        return self.schema.dump(obj)

    def update(self, obj_id, **kwargs):
        self.dao.update(obj_id, **kwargs)

    def delete(self, obj_id):
        self.dao.delete(obj_id)
