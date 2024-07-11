from datetime import datetime


def string_to_datetime(string):
    if not string:
        return None

    return datetime.strptime("".join(string), "%d.%m.%Y %H:%M:%S")


def get_seconds_from_periodicity(periodicity_unit, periodicity_value):
    seconds = {
        "секунда": 1,
        "минута": 60,
        "час": 3600,
        "день": 86400,
        "неделя": 604800,
        "месяц": 2628000,
        "год": 31536000,
    }
    return seconds[periodicity_unit] * periodicity_value
