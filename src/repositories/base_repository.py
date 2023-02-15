from abc import ABC, abstractmethod
from typing import List, Optional


class BaseRepository:
    """ An interface for a basic repository that provides CRUD (Create, Read, Update, Delete) operations. """
    @abstractmethod
    def create(self, obj) -> None:
        pass

    @abstractmethod
    def read(self, _id) -> Optional[object]:
        pass

    @abstractmethod
    def update(self, obj, _id) -> None:
        pass

    @abstractmethod
    def delete(self, _id) -> None:
        pass

    @abstractmethod
    def read_all(self) -> List[object]:
        pass
