from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Validator(ABC, Generic[T]):
    @classmethod
    @abstractmethod
    def convertToDto(cls, **kwargs) -> T:
        pass
