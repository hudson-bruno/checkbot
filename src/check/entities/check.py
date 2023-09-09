from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from uuid import UUID

from discord import Member, User


@dataclass
class Check:
    class InsertType(Enum):
        MANUAL = "MANUAL"
        AUTO = "AUTO"

    id: UUID
    user: User | Member
    date: datetime
    insert_type: InsertType
