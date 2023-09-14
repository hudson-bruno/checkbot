from datetime import datetime


def is_simple_datetime(value):
    try:
        datetime.strptime(value, "%d/%m/%y %H:%M")
    except ValueError:
        return False

    return True
