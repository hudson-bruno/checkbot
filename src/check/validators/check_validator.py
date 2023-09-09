from datetime import datetime
from typing import Optional

from discord import Member, User
from pydantic import BaseModel, ConfigDict, field_serializer


class CheckParametersValidator(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    user: User | Member
    date: Optional[str]

    @field_serializer("date")
    def serialize_dt(self, date: Optional[str], _info):
        if date is None:
            return datetime.utcnow()

        return datetime.strptime(date, "%d/%m/%y %H:%M")
