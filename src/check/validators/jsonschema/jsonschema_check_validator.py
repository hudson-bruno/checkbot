from datetime import datetime

from check.entities.check import Check
from check.use_cases.check import CheckUseCaseDTO
from core.validator import Validator
from core.validator.jsonschema.jsonschema_validator import JsonSchemaValidator
from utils.jsonschema_validate import jsonschema_validate


class JsonSchemaCheckValidator(Validator[CheckUseCaseDTO]):
    def __init__(self, **kwargs) -> None:
        self.data = kwargs
        pass

    @property
    def user(self):
        return self.data["user"]

    @property
    def date(self):
        if self.data["date"]:
            return datetime.strptime(self.data["date"], "%d/%m/%y %H:%M")

        return datetime.utcnow()

    @property
    def insert_type(self):
        return (
            Check.InsertType.AUTO
            if self.data["date"] is None
            else Check.InsertType.MANUAL
        )

    @classmethod
    def convertToDto(cls, **kwargs):
        schema = JsonSchemaValidator(
            {
                "type": "object",
                "properties": {
                    "date": {"type": ["string", "null"], "is_simple_datetime": True},
                    "test": {"type": ["int"]},
                },
            },
        )
        jsonschema_validate(schema, kwargs)

        serializer = cls(**kwargs)

        return CheckUseCaseDTO(serializer.user, serializer.date, serializer.insert_type)
