from abc import ABC, abstractmethod

from check.entities.check import Check


class CheckRepository(ABC):
    @abstractmethod
    def insert(self, check: Check) -> Check:
        pass
