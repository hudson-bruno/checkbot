from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from discord import Member, User

from check.entities.check import Check
from check.repositories.check_repository import CheckRepository


@dataclass
class CheckUseCaseDTO:
    user: User | Member
    date: datetime
    insert_type: Check.InsertType


class CheckUseCase:
    def __init__(self, repository: CheckRepository) -> None:
        self.repository = repository

    async def execute(self, dto: CheckUseCaseDTO) -> Check:
        check = Check(uuid4(), dto.user, dto.date, dto.insert_type)

        self.repository.insert(check)

        return check
