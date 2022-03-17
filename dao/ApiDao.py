
import abc

from database import db


class ApiDao(abc.ABC):

    @property
    @abc.abstractmethod
    def model(self):
        pass

    def get_objects(self, page: int = 1, page_size: int = None) -> list:
        """Retrieves specific objects from the database."""
        query = self.model.query
        if page_size:
            query = query.limit(page_size)
            if page:
                query = query.offset(page * page_size)
        return query.all()

    def insert(self, **kwargs):
        new = self.model(**kwargs)
        db.session.add(new)
        db.session.commit()

    def get_one(self, obj_id):
        return self.model.query.filter(self.model.id == obj_id).first_or_404()

    def update(self, obj_id, **kwargs):
        obj = self.get_one(obj_id)
        for attr, value in kwargs.items():
            obj.__setattr__(attr, value)
        db.session.commit()

    def delete(self, obj_id):
        obj = self.get_one(obj_id)
        db.session.delete(obj)
        db.session.commit()
