
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

    def insert(self, obj):
        """Creates object in the database."""
        self.dao.insert(**obj)

    def get_one(self, obj_id):
        """Retrieves one object from the database."""
        obj = self.dao.get_one(obj_id)
        return self.schema.dump(obj)

    def update(self, obj_id, **kwargs):
        """Updates one object in the database."""
        self.dao.update(obj_id, **kwargs)

    def delete(self, obj_id):
        """Deletes one object in the database."""
        self.dao.delete(obj_id)
