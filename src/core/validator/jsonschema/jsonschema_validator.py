from jsonschema import Draft202012Validator, ValidationError, validators

from core.validator.datetime.is_simple_datetime import is_simple_datetime


def is_simple_datetime_validator(validator, value, instance, schema):
    if instance is None:
        return

    if not is_simple_datetime(instance):
        yield ValidationError(f"{instance} does not follow format %d/%m/%y %H:%M")


all_validators = dict(Draft202012Validator.VALIDATORS)
all_validators["is_simple_datetime"] = is_simple_datetime_validator
JsonSchemaValidator = validators.create(
    meta_schema=Draft202012Validator.META_SCHEMA, validators=all_validators
)
