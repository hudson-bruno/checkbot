from core.exceptions import AppValidationError


def jsonschema_validate(schema, instance):
    errors = sorted(schema.iter_errors(instance), key=lambda e: e.path)
    if errors:
        error_msg = ""
        for error in errors:
            error_path = ".".join(error.path)
            error_msg += f"{error_path}: {error.message}\n"

        raise AppValidationError(error_msg)
