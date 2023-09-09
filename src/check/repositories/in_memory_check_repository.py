from check.entities.check import Check
from check.repositories.check_repository import CheckRepository


class InMemoryCheckRepository(CheckRepository):
    checks: list[Check] = []

    def insert(self, check: Check):
        self.checks.append(check)

        return check
